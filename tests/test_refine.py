import pytest
from refine import refine_typescript, extract_type_alias, update_imports, handle_circular_dependencies, TypeAlias

def test_extract_type_alias():
    code = """ 
class MyClass:
    my_var: int = 5 
"""
    type_alias = extract_type_alias(code)
    assert type_alias.name == "MyClass"
    assert type_alias.type == "int"

def test_update_imports():
    code = """ 
import os 
"""
    type_alias = TypeAlias("MyClass", "int")
    updated_code = update_imports(code, type_alias)
    assert "from MyClass import MyClass" in updated_code

def test_handle_circular_dependencies():
    code = """ 
class MyClass:
    my_var: MyClass = 5 
"""
    type_alias = TypeAlias("MyClass", "int")
    updated_code = handle_circular_dependencies(code, type_alias)
    assert "# Warning: circular dependency detected for MyClass" in updated_code

def test_refine_typescript():
    code = """ 
class MyClass:
    my_var: int = 5 
"""
    updated_code = refine_typescript(code)
    assert "MyClass" in updated_code
    assert "my_var" in updated_code

def test_refine_typescript_no_type_alias():
    code = """ 
class MyClass:
    pass 
"""
    updated_code = refine_typescript(code)
    assert updated_code == "No type alias found"

def test_refine_typescript_circular_dependency():
    code = """ 
class MyClass:
    my_var: MyClass = 5 
"""
    updated_code = refine_typescript(code)
    assert "# Warning: circular dependency detected for MyClass" in updated_code
