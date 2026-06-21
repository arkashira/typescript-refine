import json
from dataclasses import dataclass
from typing import List

@dataclass
class TypeScriptProject:
    name: str
    start_script: str
    build_config: str
    demo_file: str
    test_command: str

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError("Project name must be a string")
        if not self.name:
            raise ValueError("Project name cannot be empty")

    def compile_and_run(self):
        # Simulate compilation and running of the project
        return f"Compiled and ran {self.name}"

    def update_readme(self):
        # Simulate updating the README with exact commands
        return f"Updated README for {self.name}"

    def run_test(self):
        # Simulate running the test
        return f"Ran test for {self.name}"

    def validate_typescript(self):
        # Simulate validating TypeScript compilation
        return f"Validated TypeScript for {self.name}"
