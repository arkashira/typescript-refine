import ast
import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class TypeAlias:
    name: str
    type: str

def extract_type_alias(code: str) -> TypeAlias:
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for child in node.body:
                if isinstance(child, ast.AnnAssign):
                    return TypeAlias(node.name, ast.unparse(child.annotation))
    raise ValueError("No type alias found")

def update_imports(code: str, type_alias: TypeAlias) -> str:
    lines = code.splitlines()
    updated_lines = []
    for line in lines:
        if "import" in line:
            updated_lines.append(line + f"\nfrom {type_alias.name} import {type_alias.name}")
        else:
            updated_lines.append(line)
    return "\n".join(updated_lines)

def handle_circular_dependencies(code: str, type_alias: TypeAlias) -> str:
    lines = code.splitlines()
    updated_lines = []
    for line in lines:
        if type_alias.name in line:
            updated_lines.append(f"# Warning: circular dependency detected for {type_alias.name}\n" + line)
        else:
            updated_lines.append(line)
    return "\n".join(updated_lines)

def refine_typescript(code: str) -> str:
    try:
        type_alias = extract_type_alias(code)
        updated_code = update_imports(code, type_alias)
        updated_code = handle_circular_dependencies(updated_code, type_alias)
        return updated_code
    except ValueError as e:
        return str(e)
