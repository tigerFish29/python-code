from random import shuffle


def add_function(num1,num2):
    return num1*num2
result = add_function(50,2)

print(result)
# functions execute block 
def say_hello(name):
    print(f"Hello {name} hope you are well")

say_hello("Brian")

# return key word 
def add_num(num1, num2):
    return num1 + num2
    # allows you to save return as a variable 
result = add_num(5,5)
print(result)
print(type(result))

def check_even_number(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass 
    return False # complete the entire loop first 
# check if the numbers are even 
evens = check_even_number([1,2,4,8,3,9,12,6])
print(evens)

# return all the even numbers in the list 
# empty [] placeholder variables will append to it 
# return => even_numbers[] 

def check_numbers(number_list):
    # placeholder for our new numbers
    special_numbers = []
    for num in number_list:
        if num % 2 == 0:
            special_numbers.append(num)
        else:
            pass
    return special_numbers

others = check_numbers([2,3,4,6,8,60,80])
print(others)

# input from the user 
mark = int(input("Please enter your mark for the exam! "))
if mark >= 85:
    print("Distinction")
elif mark >= 65:
    print("Pass")
else:
    print("Fail")

# tuple unpacking 
work_hours = [('abby',100),('billy',500),('cassie',344)]

def employee_check(work_hours):
    current_max = 0;
    employee_of_month = ""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
        # return the employee of the month 
    return (employee_of_month,current_max)

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

example = [2,4,5,6,6,6,8,9,10]
results = shuffle_list(example)
print(results)

# nested loops 
# *args kwargs 
def more(*args):
    return sum(args) * 0.20

numbers = more(40,60,40,200)
print(numbers) # looks like a tuple 
# loop through the tuple 
# args can be anything just a placeholder pep8 
# key word arguments **kwargs 
def others(**kwargs):
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("No fruits in this section")

dict = others(fruit="apple",veggie = "lettuce")
print(dict)
# arguments and key word arguments 
# *args **kwargs check docs for this 
def myfunc(*args):
    even_numbers = []
    for numbers in args:
        if numbers % 2 == 0:
            even_numbers.append(numbers)
        else:
            pass
            #return even_numbers.append(numbers)
    return even_numbers
        
   # print(len(args))
    
more = myfunc(12,13,15,17,20,50,80,12,4,33,8,100)
print(more)

# lambda expressions filters and map 
# annonymous functions 
def square(num):
    return num**2

# define the map method 
# arrays 
numbers = [2,4,8,12,18,30,50,66,100]

# use the map method to iterate through 
for item in map(square, numbers):
    print(item)

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ["congratulations","boddy","ben","mark"]
namez = list(map(splicer,names))
print(namez) # print statement 

# numpy iterating through arrays [] 
# oop in python >> 
# great way of organising the code 
# users to create their own objects 

# repeatable and scalable code 
# functions not always enough 
class NameClass():
    def __init__(self) -> None:
        pass
            # self connect to the class 
            # init constructor 
            #  self connected to the class 
class Dog():
    def __init__(self,breed):
        self.breed = breed   

 # attributes are not executed 
 #  methods need to be executed     
 # self.name 
 #                                     
class Circle():
    # class attribute 
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
    # method 
    def getCircumference(self):
        return self.radius * self.pi * 2

# create an instance of the circle 
my_circles = Circle()
print(my_circles.getCircumference())

# special methods 
class Sample():
    pass 
# dunder methods 
class Book():
     
     def __init__(self, title):
         self.title = title

     def __str__(self):
        return f"{self.title}"
        # asking for the string reperesentation 
     #def __len__(self)

book = Book("The Monnlight")
print(book) # string version when printed 

# solution 
class Line():

    def __init__(self,coord1,coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return ((x2 -x1)**2 + (y2-y1)**2)**0.5


    def slope(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2

        return (y2-y1)/(x2-x1)

c1 = (3,2)
c2 = (8,10)

myLine = Line(c1,c2)

myLine.distance()
myLine.slope()