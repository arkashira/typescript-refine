import subprocess
import json
from dataclasses import dataclass
from typing import List

@dataclass
class RefactorResult:
    success: bool
    error_report: str

def apply_refactor(refactor_command: str) -> None:
    subprocess.run(refactor_command, shell=True)

def run_type_check() -> RefactorResult:
    try:
        output = subprocess.check_output(['tsc', '--noEmit'], stderr=subprocess.STDOUT)
        return RefactorResult(True, '')
    except subprocess.CalledProcessError as e:
        error_report = e.output.decode('utf-8')
        return RefactorResult(False, error_report)

def refactor_with_validation(refactor_command: str) -> RefactorResult:
    apply_refactor(refactor_command)
    result = run_type_check()
    if not result.success:
        # Roll back changes
        subprocess.run('git reset --hard', shell=True)
    return result
