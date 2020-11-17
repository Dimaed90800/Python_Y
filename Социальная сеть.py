class User:
    def __init__(self, name):
        self.name = name
        
    def send_message(self,user, message):
        pass
    
    def post(self, message):
        pass
    
    def info(self):
        return ""
    
    def describe(self):
        print(self.info())

class Person(User):
    def __init__(self, name, birthday):
        super().__init__(name)
        self.birthday=birthday
    
    def info(self):
        return  "Дата рождения: "+str(self.birthday)
    
    def subscribe(self, user):
        pass

class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description=description
    
    def info(self):
        return "Описание: "+str(self.description)
    
    