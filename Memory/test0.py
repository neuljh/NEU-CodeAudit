import clang.cindex
import os


def check_memory_leak(file_path):
    index = clang.cindex.Index.create()
    translation_unit = index.parse(file_path)

    for diag in translation_unit.diagnostics:
        if diag.severity >= clang.cindex.Diagnostic.Warning:
            print(diag.spelling)

    for node in translation_unit.cursor.walk_preorder():
        if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
            function_name = node.spelling
            if "malloc" in function_name or "calloc" in function_name or "realloc" in function_name:
                for child in node.get_children():
                    if child.kind == clang.cindex.CursorKind.RETURN_STMT:
                        if "NULL" not in child.spelling:
                            print(f"Memory leak detected in function {function_name}")
                            print(f"Allocated memory not freed in function {function_name}")
                            print(f"Line number: {child.location.line}")
                            print(f"File path: {file_path}")
                            print()
                            break


file_path = "../test.c"
check_memory_leak(file_path)



