from typescript_refine import TypeScriptProject
import pytest
import sys
sys.path.insert(0, './src')

def test_compile_and_run():
    project = TypeScriptProject("test-project", "start-script", "build-config", "demo-file", "test-command")
    result = project.compile_and_run()
    assert result == "Compiled and ran test-project"

def test_update_readme():
    project = TypeScriptProject("test-project", "start-script", "build-config", "demo-file", "test-command")
    result = project.update_readme()
    assert result == "Updated README for test-project"

def test_run_test():
    project = TypeScriptProject("test-project", "start-script", "build-config", "demo-file", "test-command")
    result = project.run_test()
    assert result == "Ran test for test-project"

def test_validate_typescript():
    project = TypeScriptProject("test-project", "start-script", "build-config", "demo-file", "test-command")
    result = project.validate_typescript()
    assert result == "Validated TypeScript for test-project"

def test_invalid_project_name():
    with pytest.raises(TypeError):
        TypeScriptProject(123, "start-script", "build-config", "demo-file", "test-command")

def test_empty_project_name():
    with pytest.raises(ValueError):
        TypeScriptProject("", "start-script", "build-config", "demo-file", "test-command")
