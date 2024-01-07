class Person():
    def __init__(self,name) -> None:
        pass


class Teacher(Person):
    def __init__(self, name,) -> None:
        super().__init__(name)
        
        



    def take_exam(self,classroom,subject):
        pass



class Student(Person):
    def __init__(self, name,classroom,subject) -> None:
        super().__init__(name)
        self.classroom=classroom
        self.subject=subject