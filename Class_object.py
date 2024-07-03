class Robot:
    '''This is class implemented by Robot.'''
    
    def __init__(self, n, y):
        self.name=n
        self.year=y

    
        


r1=Robot('Albert', 2024)
print(r1.__doc__)
print(r1.name, r1.year)
print(r1.__dict__)  # print the attributes of the object as a dictionary.

