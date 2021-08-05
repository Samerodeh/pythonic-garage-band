from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod

class Band():
    band_name=[]
    member_name=[]
    
    def __init__(self,name="unknown"):
        self.name=name
        Band.band_name.append(self)
    
    def insert(self,name1):
        self.name1=name1
        Band.member_name.append(name1)
    
    def play_solos(self):
        result=""
        for i in Band.member_name:
            result+= f"{i.play_solo()}\n"
        return result
    
    @classmethod 
    def to_list(cls):
        return cls.member_name

    def __str__(self):
        return "Band--->{self.name}"
    
    def __repr__(self):
        return "{self.name}"

class Musician():
    
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def __str__(self):
        return "Musician--->{self.name}"
    
    @abstractmethod
    def __repr__(self):
        return "{self.name}"
    
    def play_solo(self):
        return f'{self.name}'

class Guitarist(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return f"Guitarist--->{self.name}"
    
    def __repr__(self):
        return "{self.name}"
    
    def get_instrument(self):
        return "Guitarist"

class Bassist(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return f"Bassist--->{self.name}"
    
    def __repr__(self):
        return f"{self.name}"
    
    def get_instrument(self):
        return "Bassist"

class Drummer(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return f"Drummer--->{self.name}"
    
    def __repr__(self):
        return f"{self.name}"
    
    def get_instrument(self):
        return "Drummer"

if __name__=="__main__":
    pass