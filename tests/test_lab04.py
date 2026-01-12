"""
Lab 04: Text Search - Auto-grading Tests
"""

import pytest
import os
import nbformat

# Get paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOK_PATH = os.path.join(BASE_DIR, 'exercise', 'Lab04_Exercise.ipynb')


@pytest.fixture(scope="session")
def student_namespace():
    """Execute student notebook and return namespace with variables."""
    
    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    namespace = {'__name__': '__main__'}
    
    original_dir = os.getcwd()
    exercise_dir = os.path.join(BASE_DIR, 'exercise')
    os.chdir(exercise_dir)
    
    try:
        for cell in nb.cells:
            if cell.cell_type == 'code':
                if '# Quick check' in cell.source or '# Verification' in cell.source:
                    continue
                try:
                    exec(cell.source, namespace)
                except Exception as e:
                    print(f"Cell execution warning: {e}")
    finally:
        os.chdir(original_dir)
    
    return namespace


class TestExercise1:
    """Test Exercise 1: Check Text Exists (25 points)"""
    
    def test_has_fever_exists(self, student_namespace):
        assert 'has_fever' in student_namespace, "Variable 'has_fever' not found"
    
    def test_has_fever_is_bool(self, student_namespace):
        assert isinstance(student_namespace.get('has_fever'), bool), "'has_fever' should be a boolean"
    
    def test_has_fever_value(self, student_namespace):
        assert student_namespace.get('has_fever') == True, "'has_fever' should be True"


class TestExercise2:
    """Test Exercise 2: Count Occurrences (25 points)"""
    
    def test_the_count_exists(self, student_namespace):
        assert 'the_count' in student_namespace, "Variable 'the_count' not found"
    
    def test_the_count_is_int(self, student_namespace):
        assert isinstance(student_namespace.get('the_count'), int), "'the_count' should be an integer"
    
    def test_the_count_value(self, student_namespace):
        assert student_namespace.get('the_count') == 3, f"'the_count' should be 3, got {student_namespace.get('the_count')}"


class TestExercise3:
    """Test Exercise 3: Search Function (25 points)"""
    
    def test_simple_search_exists(self, student_namespace):
        assert 'simple_search' in student_namespace, "Function 'simple_search' not found"
    
    def test_simple_search_callable(self, student_namespace):
        assert callable(student_namespace.get('simple_search')), "'simple_search' should be a function"
    
    def test_simple_search_finds_match(self, student_namespace):
        func = student_namespace.get('simple_search')
        if func:
            assert func('fever', 'Patient has FEVER') == True, "simple_search should find 'fever' in 'Patient has FEVER'"
    
    def test_simple_search_no_match(self, student_namespace):
        func = student_namespace.get('simple_search')
        if func:
            assert func('cough', 'Patient has fever') == False, "simple_search should not find 'cough' in 'Patient has fever'"


class TestExercise4:
    """Test Exercise 4: Multi-Document Search (25 points)"""
    
    def test_search_docs_exists(self, student_namespace):
        assert 'search_docs' in student_namespace, "Function 'search_docs' not found"
    
    def test_search_docs_callable(self, student_namespace):
        assert callable(student_namespace.get('search_docs')), "'search_docs' should be a function"
    
    def test_search_docs_returns_list(self, student_namespace):
        func = student_namespace.get('search_docs')
        documents = student_namespace.get('documents', [])
        if func and documents:
            result = func('fever', documents)
            assert isinstance(result, list), "search_docs should return a list"
    
    def test_search_docs_correct_count(self, student_namespace):
        func = student_namespace.get('search_docs')
        documents = student_namespace.get('documents', [])
        if func and documents:
            result = func('fever', documents)
            assert len(result) == 2, f"search_docs('fever', documents) should return 2 docs, got {len(result)}"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
