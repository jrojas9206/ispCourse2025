'''
Task

Write an application to manage the students grades along the whole school year. 

Student is a class that contain the attributes 
Name: str
School year: int 
Age: int
Total Grade: float
Classes  : dict 
Classroom : str
Contain the methods 
setCourses 
setGrades 
getCourses 
get Grades 
UpdateGrades 
displayReport

Create a class Curse that consume the class Student. 

Methods 
addStudent
GetStudentReport 
updateStudent
removeStudent 

'''
import sys 

class Student(object):

    def __init__(self, name:str, age:int, school:str='sk', course:str='') -> None:
        self._name = name 
        self._school = school
        self._age = age 
        self._totalGrade = -1 
        self._classRoom = ""
        self._course = course
        self._dictCourses = {}

    def setCourse(self, courseId:str) -> None:
        self._course = courseId
        
    def setGrades(self, dictCourses:dict) -> None:
        self._dictCourses = dictCourses

    def getName(self) -> str:
        return self._name

    def display(self):
        print(f'Name: {self._name}')
        print(f'School: {self._school}')
        print(f'Course: {self._course}' )


class Course(object):

    def __init__(self, myFirtStudet:Student):
        self.studentsList = [myFirtStudet]

    def addStudent(self, newStudent:Student) -> None:
        self.studentsList.append(newStudent)

    def searchStudent(self, name:str) -> Student:
        for currentStudent in self.studentsList:
            if currentStudent.getName() == name:
                return currentStudent
        return None 

def main():
    print('-----------------')
    print('Example student object')    
    print('-----------------')
    varStudent = Student('Pablo',
                         age=1, 
                         school='MU')
    varStudent.setCourse('ISP2025PY')

    varStudent.display()

    db = Course(varStudent)

    student2 = Student('Juan',
                         age=2, 
                         school='UM2')
    db.addStudent(student2)
    print('-----------------')
    print('Searched student')    
    print('-----------------')
    searchedStudent = db.searchStudent('Juan')

    searchedStudent.display()
    return 0

if __name__ == "__main__":
    sys.exit(main())

'''
How will you create a unique ID for each element of the class study??

How will you add the method removeStudent on the class Course??
'''