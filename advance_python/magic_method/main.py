

class Person:
    def __init__(self , fname ,lname  ):
        self.fname = fname
        self.lname = lname

    
    # thiis used for developer for debugging 
    def __repr__(self):
        return"Person first name is {} and last name is {}".format(self.fname  , self.lname)
        
# thisis used for printing  for end user
    def __str__(self):
        return self.fname + self.lname

    

if __name__ == "__main__":
    p1 = Person("Anupam", "Baral")
    print(p1)

    print([p1])
