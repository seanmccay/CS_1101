number1 = 100  # global variable

def main():
    number = 500  # local variable because it's instantiated inside of a function.
    number1 = 200  # Here I just edited the global variable, number1

def getName():
    number = 300  # local variable
    number = 1
    number = 25
    # you can see that our variables can be changed as many times as we want


number = 600  # does not edit the previous local variables. It creates a new one in the global scope.


# I created two local variables using the same name in main() and getName().
# Even though they have the same name, they refer to different variables in memory.
# Note that having all of these variables with the same name is a very bad practice, just doing it to
# demonstrate global vs local scope.

# Hope this helps!

