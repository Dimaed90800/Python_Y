class Profile():
    def __init__(self, job):
        self.job=job
        
    def info(self):
        return ''
    
    def describe(self):
        print(self.info())
        
class Vacancy(Profile):
    
    def __init__(self, job, salary):
        super().__init__(job)
        self.salary=salary
        
    def info(self):
        return "Предлагаемая зарплата: "+str(self.salary)
    
class Resume(Profile):
    
    def __init__(self, job, expirience):
        super().__init__(job)
        self.expirience=expirience
        
    def info(self):
        return  "Стаж работы: "+str(self.expirience)