from examples.student import Student

def test_introduce_and_update_major():
    s = Student('Max', 'Math', 3.0)
    assert 'Max' in s.introduce()
    s.update_major('CS')
    assert 'CS' in s.introduce()

def test_add_grade_updates_gpa():
    s = Student('Sophia', 'CS', 3.0)
    s.add_grade(95, 100)
    assert s.gpa > 3.0
