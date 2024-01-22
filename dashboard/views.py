
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.models import Language
from .models import Question
from .utils import run_code

# Create your views here.


@login_required(redirect_field_name="login")
def app(request):
    return render(request, template_name='students/home.html')


@login_required(redirect_field_name="login")
def test(request, slug, question_num):
    language = Language.objects.get(slug=slug)
    question = Question.objects.filter(
        language=language, question_number=question_num).first()
    if request.method == "POST":
        code = request.POST.get("code")
        time = request.POST.get("timeCounter")
        # code += f"\n\n\nsolution({question.input1})"
        output = run_code(code, question.input1, question.expected_output1)
        print(output, time)
        return redirect("test", language.slug, question_num+1)

    if question == None:
        return redirect("app")
    context = {
        'language': language,
        'question': question
    }
    return render(request, template_name='students/test.html', context=context)


# def submission(request):


#     return redirect("test")
# if __name__ == "__main__":
#     # Example usage
#     code = """
# def add(a, b):
#     return a + b

# print(add(2, 3))
# """
#     input_data = ""
#     expected_output = "5"

#     if run_code(code, input_data, expected_output):
#         print("Code executed successfully and produced the expected output.")
#     else:
#         print("Code did not produce the expected output.")
