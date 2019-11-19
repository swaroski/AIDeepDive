#1) function that converts the argument into a string
def convert_to_string(string):
    return str(string)

#2) function that takes two lists as arguments,
    # checks whether the two lists have overlapping elements
    # and either returns the duplicated elements or provides a nice message

a = []
b = []

def two_lists(a,b):
    #a = []
    #b = []
    if a == b:
        return a, b
    else:
        print("Go to hell")


# Create a function that tries to replace index 0 of the argument passed
   # with the word "pancakes"
def pancakes(mylist):
    mylist[0] = "pancakes"
    return mylist
pancakes([1,2,3])

