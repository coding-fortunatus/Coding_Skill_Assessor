import ast
import autopep8
import os


def extract_variables(filename) -> set:
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
    with open(filename, 'r') as file:
        tree = ast.parse(file.read(), filename=filename)

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


def check_autopep8_conformance(filename) -> bool:
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
    with open(filename, 'r') as file:
        original_code = file.read()

    formatted_code = autopep8.fix_code(original_code)

    return original_code == formatted_code


def evaluate_script(filename) -> bool:
    """
    Definition:
        Evaluate a Python script for variable naming convention and autopep8 conformance.
    \n\n
    Parameters:
        filename (str): The path to the Python script.
    \n\n
    Returns:
        bool: True if the script adheres to the specified standards, False otherwise.
    """
    variables = extract_variables(filename)
    naming_convention_check = check_variable_naming_convention(variables)
    autopep8_conformance_check = check_autopep8_conformance(filename)

    return naming_convention_check and autopep8_conformance_check


def evaluate_scripts_in_directory(directory) -> dict:
    """
    Definition:
        Function to evaluate python scripts in a specific directory while conforming to some evaluation metrics.\n\n
    Parameters:
        directory (str): The path to the directory containing Python scripts. \n\n
    Returns:
        dict: A dictionary where script filenames are keys, and values are boolean results of the evaluation.
    """
    results = {}

    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            filepath = os.path.join(directory, filename)
            results[filename] = evaluate_script(filepath)

    return results


# Testing out the evaluation script
if __name__ == "__main__":
    directory_path = "/home/fortunatus/Documents/Variabe Evaluation/question answers"
    evaluation_results = evaluate_scripts_in_directory(directory_path)

    print("Evaluation Results:")
    for filename, result in evaluation_results.items():
        print(f"{filename}: {result}")
