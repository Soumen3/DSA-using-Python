# Pass by object reference (mutable object)
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

# Pass by object reference (immutable object)
def modify_string(s):
    s += " World"
    print("inside function: ",s)

my_string = "Hello"
modify_string(my_string)
print("outside the function: ",my_string)  # Output: Hello (original string is not modified)

# Pass by object reference (mutable object)
def modify_dict(d):
    d["key"] = "new value"

my_dict = {"key": "old value"}
modify_dict(my_dict)
print(my_dict)  # Output: {'key': 'new value'}
