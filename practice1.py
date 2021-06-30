import time

print("Hello world!")

numb=5
if numb%2==0:
    print("even")
else:
    print("odd")

not(5 and 10)
3 or 6

time.sleep(5) #import time 

list=[1,2,3,6,5]
if 5 in list:
    print("5 is in list", end="\n\n")

lst=[]
if lst: #can do "if lst is None:" but use is and not == 
    print(lst) #will print lst if not empty

#can do nice stuff like if 0 < num < 100 and it wil work how you would expect


class Number:
    def __init__(self, num): #convention: call it "self" but you could call it whatever you want
        self.num = num
    
    def is_even(self): #functions: I think you have to pass "self" first always, then whatever else
        return self.num % 2 == 0
#you can create members on the fly -- careful of typos = new member
#classes are still a little fuzzy

num = Number(5)
print(num.is_even()) #calls is even with num which is of the Number class and it is 5 
    #this could look like Number.is_even(num) but it figures that out for you
