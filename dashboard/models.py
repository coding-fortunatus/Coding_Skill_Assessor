import uuid
from django.db import models
from home.models import Language
# Create your models here.


class Question(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    language = models.ForeignKey(
        Language, related_name="language_question", on_delete=models.CASCADE)
    question_number = models.PositiveSmallIntegerField()
    question_text = models.CharField(max_length=1000)
    question_description = models.TextField()
    starter_code = models.TextField()
    expected_time = models.PositiveSmallIntegerField()
    input1 = models.CharField(max_length=1000, default="")
    input2 = models.CharField(max_length=1000, default="")
    input3 = models.CharField(max_length=1000, default="")
    expected_output1 = models.CharField(max_length=1000)
    expected_output2 = models.CharField(max_length=1000)
    expected_output3 = models.CharField(max_length=1000)
