class Teacher : 
    def __init__(self, name, subject) : 
        self.name : name
        self.subject : subject
        
    def __str__(self) : 
        return f'교사 이름 : {self.name}, 과목 : {self.subject}'
    
class Student : 
    def __init__(self, name, student_id) : 
        self.name = name
        self.student_id = student_id
        
    def __str__(self) : 
        return f'학생 이름 : {self.name}, ID : {self.student_id}'
    
class Academy : 
    def __init__(self) :
        self.teacher = None
        self.students= []
        
    