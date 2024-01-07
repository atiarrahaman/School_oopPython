class School():
    def __init__(self,name) -> None:
        self.name=name
        self.classRooms={}



    def Add_classroom(self,classRoom):
        self.classRooms[classRoom.name]=classRoom
        print(self.classRooms)
    
    def student_admition(self,student,classroom):
        if classroom in self.classRooms:
            self.classRooms[classroom].add_student(student)


class Class_Rooms():
    def __init__(self,name) -> None:
        self.name=name
        self.students=[]
        self.classroom=[]


    def add_student(self,student):
        seliar_id=f'{self.name} -{len(self.students) +1 }'

        self.students.append(student)

    
    def add_sub(self,subject):
        self.classroom=subject
        print(self.classroom.name)

    def __str__(self) -> str:
        return f'{self.name} -{len(self.students)}'
    

class Subject():
    def __init__(self,name) -> None:
        self.name=name
        self.subject=[]
        self.student=[]
    

    def add_teacher(self,teacher):
        self.subject=teacher
        print(self.subject)

