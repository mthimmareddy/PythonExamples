

class Animal:
    def __init__(self,breed,color,age):
        self.type=type
        self.color=color
        self.age=age
        
    def getnames(self):
         print self.type
         
         
class Dog(Animal):
    def __init__(self,breed,color,age,owner): 
       Animal.__init__(self,breed,color,age)
       self.owner=owner  
    def getowner(self):
         print self.owner     
         
#cat=Animal("dog" ,"brown",3)  
#cat.getnames() 

dog=Dog("dog" ,"brown",3,"manju")   
dog.getowner() 
print dog.color
