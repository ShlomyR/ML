import random

class Number:   
    def __init__(self, FS,SS ): 
        self.FS = FS    
        self.SS = SS    
        self.steatment = [[0] for i in range(self.FS)]


number = int(input("waht's up bro? "))
n = 0
i = 5
while n <= 5:   
    if number < i:  
#        number1 = input("glad to hear! ")
        print("what")
    elif number == i:   
        print("yo") 
    else:   
        print("ok")
    n = n + 1
    
print("done! ")    

'''s = 8
n = 0
i = 5
num =' why?'
num1 = 'nice!'
num3 = 'great!!!'


while n < i:
    guess = int(input('Guess: '))
    n += 1  
    if guess == s:
        print(num3)
        break
else:   
    print('done!')'''

