import sys
import io
import ast
import autopep8
import os


def extract_variables(code) -> set:
    """
    Definition:
        Function to extract variables from any python scrpit using the python ast library.
        Set is used to collect unique variable names found in the Python scripts within the specified directory. \n\n
        The uniqueness property of sets ensures that each variable name is considered only once during subsequent analysis, making it a suitable data structure for this purpose. \n\n
        isinstance() function is commonly used for type checking in Python programs, especially in situations where you want to ensure that an object is of a specific type before performing certain operations on it.\n\n
    Parameters:
        filename (str): The path to the Python script.\n\n
    Returns:
        set: Unique values of varibles in the file.
    """
    tree = ast.parse(code)

    variables = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variables.add(target.id)

    return variables


def check_variable_naming_convention(variables) -> bool:
    """
    Definition:
        Function to check if a variable name conforms with the variable naming convention using isidentifier(). This method is particularly useful when you want to check if a string can be used as a variable name in Python. It checks for conditions such as whether the string starts with an underscore or a letter, and the subsequent characters are either letters, digits, or underscores. \n\n
    Parameters:
        variables (set): Set of all variables in a script.\n\n
    Returns:
        bool: True if the script adheres to variable naming conventions, False otherwise.
    """
    for variable in variables:
        if not variable.isidentifier() or not variable.islower():
            return False
    return True


def check_autopep8_conformance(code) -> bool:
    """
    Definition:
        The autopep8.fix_code function is part of the autopep8 library in Python, and it is used to automatically format Python code according to the PEP 8 style guide. \n\n
    Note:
        PEP8 is the style guide for Python code, and it defines the recommended conventions for writing readable and consistent code.\n\n
    Parameters:
        filename (str): The path to the Python script.\n\n
    Returns:
        bool: True if the script adheres to PEP 8 standards, False otherwise.
    """
    formatted_code = autopep8.fix_code(code).strip()

    return code == formatted_code


def run_code(code, input_data, expected_output):
    try:
        # Redirect stdout to capture the output
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # Redirect stdin to provide input data
        original_stdin = sys.stdin
        sys.stdin = io.StringIO(input_data)

        # Execute the code
        exec(code)

        # Capture the output
        actual_output = sys.stdout.getvalue()

        # Compare the actual output with the expected output
        # return actual_output.strip() == expected_output.strip()
        return True, actual_output.strip()

    except Exception as e:
        return False, f"Error: {str(e)}"

    finally:
        # Restore stdout and stdin
        sys.stdout = original_stdout
        sys.stdin = original_stdin


class CodingAgent:
    def __init__(self):
        pass

    def assess_variable_declaration(self, code):
        # Placeholder logic for assessing variable declaration
        variables = extract_variables(code=code)
        naming_convention = check_variable_naming_convention(
            variables=variables)
        if naming_convention:
            return 10
        return 2

    def assess_coding_standards(self, code):
        is_standard = check_autopep8_conformance(code)
        if is_standard:
            return 20
        return 0

    def assess_optimization(self, code):
        # Placeholder logic for assessing optimization
        # (Replace with actual implementation)
        return 25  # Placeholder score between 0 and 1

    def assess_speed(self, time, expected_time):
        if time <= expected_time:
            return 15
        elif time <= expected_time + expected_time / 2:
            return 8
        return 0  # Placeholder score between 0 and 1

    def assess_correctness(self, code, input_data, expected_output):
        # Placeholder logic for assessing correctness
        is_correct, output = run_code(
            code=code, input_data=input_data, expected_output=expected_output)
        if is_correct:
            return 30
        return 0  # Placeholder score between 0 and 1


def assess_student_code(agent, student_code):
    variable_declaration_score = agent.assess_variable_declaration(
        student_code)
    coding_standards_score = agent.assess_coding_standards(student_code)
    optimization_score = agent.assess_optimization(student_code)
    speed_score = agent.assess_speed(student_code)
    correctness_score = agent.assess_correctness(student_code)

    # Apply weights to each KPI score based on specified percentages
    overall_score = (
        variable_declaration_score +
        coding_standards_score +
        speed_score +
        optimization_score +
        correctness_score
    )

    return overall_score, variable_declaration_score, coding_standards_score, optimization_score, speed_score, correctness_score


# # Example usage:
# coding_agent = CodingAgent()
# student_code_submission = """
# # Paste student code here
# """

# result = assess_student_code(coding_agent, student_code_submission)
# print(f"Overall Assessment Score: {result}")
