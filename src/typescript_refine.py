import json
import os
from dataclasses import dataclass
from typing import Dict

@dataclass
class TechnicalDebtScore:
    score: int
    details: Dict[str, int]

def calculate_technical_debt_score(file_content: str) -> TechnicalDebtScore:
    # Simplified calculation for demonstration purposes
    cyclomatic_complexity = file_content.count('if') + file_content.count('for')
    any_type_usage = file_content.count('any')
    score = cyclomatic_complexity + any_type_usage
    details = {
        'cyclomatic_complexity': cyclomatic_complexity,
        'any_type_usage': any_type_usage
    }
    return TechnicalDebtScore(score, details)

def update_status_bar_indicator(file_path: str) -> TechnicalDebtScore:
    with open(file_path, 'r') as file:
        content = file.read()
    return calculate_technical_debt_score(content)

def show_tooltip(score: TechnicalDebtScore) -> str:
    return json.dumps(score.__dict__, indent=2)

def open_debt_dashboard_panel() -> None:
    print("Opening debt dashboard panel...")
