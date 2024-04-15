from __future__ import annotations
class Student:
    def __init__(self, name: str, courses: int) -> None:
        self.name = name
        self.courses = courses

    def __add__(self, student: Student) -> Student:
        return Student("name",(self.courses + student.courses))
        
    def __str__(self) -> str:
        return f"{self.courses}"

    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, student: Student) -> bool:
        return self.courses < student.courses

    def __eq__(self, student: Student) -> bool:
        if isinstance(student,Student):
            return self.courses == student.courses
        else:
            return False

    def __ne__(self, student: Student) -> bool:
        return self.courses != student.courses

    def __gt__(self, student: Student) -> bool:
        return self.courses > student.courses
    
def main():
    a = Student('Peter', 3)
    b = Student('Mike', 4)
    c = Student('John', 5)
    d = Student('Kelvin', 3)

    print(a + b + d) 
    print(a != d)     
    print(b < c)  
    print(b == c)
    print(a == d)    

main()