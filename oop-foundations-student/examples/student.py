class Student:
    def __init__(self, name: str, major: str, gpa: float = 0.0):
        self.name = name
        self.major = major
        self.gpa = gpa

    def introduce(self) -> str:
        return f"Hi, I'm {self.name}, a {self.major} major with GPA {self.gpa:.2f}."

    def update_major(self, new_major: str) -> None:
        self.major = new_major

    def add_grade(self, points_earned: float, points_possible: float) -> None:
        if points_possible <= 0:
            raise ValueError("points_possible must be > 0")
        # naive running GPA; for teaching only
        course_gpa = (points_earned / points_possible) * 4.0
        self.gpa = (self.gpa + course_gpa) / 2.0


if __name__ == '__main__':
    s = Student('Nasara', 'CS', 3.6)
    print(s.introduce())
    s.update_major('Software Engineering')
    s.add_grade(90, 100)
    print(s.introduce())
