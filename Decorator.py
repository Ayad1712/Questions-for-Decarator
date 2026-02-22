#Questions:
#1. A decarator is a wrapper in python that does something extra with the code.
#2. We use the @ symbol to apply a decarator.
#3. The function changes what it does (without changing its own code).
#4. True
#5. To make the code more modular.
#6. C
#7. It will print "Hello!"
#8. The loud function will run the wrapper function, which will make an output, then takes and prints the output of another function, and responds to it by returning something.
#9. It doesn't return anything after func() is called.
#10. When my_decorator is called, it will print "Before", then "Hi", then "After".
#11. 
def star_decorator(func):
    def wrapper2():
        print("*****")
        func()
        print("*****")
    return wrapper2
@star_decorator
def star_function():
    print("Stars")
star_function()
#12
import time
def timer(func):
    def time_wrapper():
        print("Function Started")
        func()
        print("Function Ended")
    return time_wrapper
@timer
def time_func():
    time.sleep(3)
time_func()
#13.
def count_decorator(func):
    count = 0
    def counter_wrapper():
        nonlocal count
        count += 1
        print("Function was called ", count, " time(s)")
        func()
    return counter_wrapper
@count_decorator
def count_func():
    print("Inside the function")

count_func()
count_func()
count_func()



    
#14.
def no_run(func):
    def no_runner():
        print("Function is blocked")
        #there is no func()
    return no_runner
@no_run
def malicious():
    while True:
        print("Virus")
malicious()
#15.
def teacher_decorator(func):
    def teacher_wrapper():
        is_teacher = input(print("Is the teacher here? True or False"))
        if is_teacher == "True":
            print("is_teacher is true.")
        func()
    return teacher_wrapper
@teacher_decorator
def main3():
    print("Counting teacher...")
    time.sleep(2)
main3()
#Global and nonlocal makes variable global (acessible by other functions and used in most topics)
