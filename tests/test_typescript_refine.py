import json
from typing import Dict
from unittest.mock import MagicMock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.typescript_refine import calculate_technical_debt_score, update_status_bar_indicator, show_tooltip, open_debt_dashboard_panel

def test_calculate_technical_debt_score():
    file_content = """ if (condition) { // some code } for (let i = 0; i < array.length; i++) { // loop code } let variable: any; """
    expected_score = calculate_technical_debt_score(file_content)
    assert expected_score.score == 3
    assert expected_score.details == {'cyclomatic_complexity': 2, 'any_type_usage': 1}

def test_update_status_bar_indicator(tmpdir):
    file_path = tmpdir.join("test.ts")
    file_content = """ if (condition) { // some code } for (let i = 0; i < array.length; i++) { // loop code } let variable: any; """
    file_path.write(file_content)
    expected_score = calculate_technical_debt_score(file_content)
    actual_score = update_status_bar_indicator(str(file_path))
    assert actual_score.score == expected_score.score
    assert actual_score.details == expected_score.details

def test_show_tooltip():
    score = calculate_technical_debt_score(""" if (condition) { // some code } for (let i = 0; i < array.length; i++) { // loop code } let variable: any; """)
    expected_tooltip = json.dumps({'score': score.score, 'details': score.details}, indent=2)
    actual_tooltip = show_tooltip(score)
    assert actual_tooltip == expected_tooltip

def test_open_debt_dashboard_panel(capsys):
    open_debt_dashboard_panel()
    captured = capsys.readouterr()
    assert captured.out == "Opening debt dashboard panel...\n"
