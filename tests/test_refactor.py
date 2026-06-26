import pytest
from refactor import refactor_with_validation, RefactorResult
import subprocess

@pytest.fixture
def mock_refactor_command():
    return 'echo "Refactor applied"'

@pytest.fixture
def mock_tsc_command():
    return 'echo "Type check passed"'

def test_refactor_with_validation_success(mock_refactor_command, mock_tsc_command, monkeypatch):
    def mock_subprocess_run(command, **kwargs):
        if command == mock_refactor_command:
            return subprocess.CompletedProcess(command, returncode=0)
        elif command == ['tsc', '--noEmit']:
            return subprocess.CompletedProcess(command, returncode=0)
    monkeypatch.setattr('subprocess.run', mock_subprocess_run)
    result = refactor_with_validation(mock_refactor_command)
    assert result.success
    assert result.error_report == ''

def test_refactor_with_validation_failure(mock_refactor_command, monkeypatch):
    def mock_subprocess_run(command, **kwargs):
        if command == mock_refactor_command:
            return subprocess.CompletedProcess(command, returncode=0)
        elif command == ['tsc', '--noEmit']:
            raise subprocess.CalledProcessError(1, command, b'Type check failed')
    monkeypatch.setattr('subprocess.run', mock_subprocess_run)
    result = refactor_with_validation(mock_refactor_command)
    assert not result.success
    assert result.error_report == 'Type check failed'

def test_refactor_with_validation_rollback(mock_refactor_command, monkeypatch):
    def mock_subprocess_run(command, **kwargs):
        if command == mock_refactor_command:
            return subprocess.CompletedProcess(command, returncode=0)
        elif command == ['tsc', '--noEmit']:
            raise subprocess.CalledProcessError(1, command, b'Type check failed')
        elif command == 'git reset --hard':
            return subprocess.CompletedProcess(command, returncode=0)
    monkeypatch.setattr('subprocess.run', mock_subprocess_run)
    result = refactor_with_validation(mock_refactor_command)
    assert not result.success
    assert result.error_report == 'Type check failed'
