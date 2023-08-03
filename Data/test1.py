import re


def get_header_files(file_content):
    header_files = re.findall(r'#include\s+<(.+?)>', file_content)
    return header_files


def get_variable_names(file_content):
    variable_names = re.findall(r'\b(\w+)\b\s*;', file_content)
    return variable_names


def get_macro_definitions(file_content):
    macro_definitions = re.findall(r'#define\s+(\w+)', file_content)
    return macro_definitions


def get_function_declarations(file_content):
    function_declarations = re.findall(r'\b(\w+)\b\s*\(', file_content)
    return function_declarations


file_content = """
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

int main() {
    int num1, num2;
    float result;

    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    result = num1 + num2;

    printf("Sum: %f", result);

    return 0;
}
"""

header_files = get_header_files(file_content)
variable_names = get_variable_names(file_content)
macro_definitions = get_macro_definitions(file_content)
function_declarations = get_function_declarations(file_content)

print("Header Files:", header_files)
print("Variable Names:", variable_names)
print("Macro Definitions:", macro_definitions)
print("Function Declarations:", function_declarations)
