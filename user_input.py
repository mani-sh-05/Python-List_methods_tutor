# Q: make a program which takes values from user and creates a list and then user can select functions like remove or append etc and can apply them on the above list and at last have to print both the initial and the last modified list.
ils = []
lessons = {
    "append": {
        "definition": "Adds an element to the end of the list.",
        "syntax": "list_name.append(object)",
        "example": """
x = [1, 2, 3]
x.append(4)
print(x)

Output:
[1, 2, 3, 4]
""",
    },
    "remove": {
        "definition": "Removes the first occurrence of a specified element.",
        "syntax": "list_name.remove(object)",
        "example": """
x = [1, 2, 3, 2]
x.remove(2)
print(x)

Output:
[1, 3, 2]
""",
    },
    "insert": {
        "definition": "Inserts an element at a specific index.",
        "syntax": "list_name.insert(index, object)",
        "example": """
x = [1, 2, 3]
x.insert(1, 100)
print(x)

Output:
[1, 100, 2, 3]
""",
    },
    "pop": {
        "definition": "Removes and returns an element from a given index. By default removes the last element.",
        "syntax": "list_name.pop(index)",
        "example": """
x = [1, 2, 3]
x.pop()
print(x)

Output:
[1, 2]
""",
    },
    "clear": {
        "definition": "Removes all elements from the list.",
        "syntax": "list_name.clear()",
        "example": """
x = [1, 2, 3]
x.clear()
print(x)

Output:
[]
""",
    },
    "sort": {
        "definition": "Sorts the list in ascending order.",
        "syntax": "list_name.sort()",
        "example": """
x = [5, 2, 8, 1]
x.sort()
print(x)

Output:
[1, 2, 5, 8]
""",
    },
    "reverse": {
        "definition": "Reverses the order of elements in the list.",
        "syntax": "list_name.reverse()",
        "example": """
x = [1, 2, 3]
x.reverse()
print(x)

Output:
[3, 2, 1]
""",
    },
    "count": {
        "definition": "Returns the number of times an element appears in the list.",
        "syntax": "list_name.count(object)",
        "example": """
x = [1, 2, 2, 3, 2]
print(x.count(2))

Output:
3
""",
    },
    "index": {
        "definition": "Returns the index of the first occurrence of an element.",
        "syntax": "list_name.index(object)",
        "example": """
x = ['a', 'b', 'c']
print(x.index('b'))

Output:
1
""",
    },
    "extend": {
        "definition": "Adds all elements from another iterable to the end of the list.",
        "syntax": "list_name.extend(iterable)",
        "example": """
x = [1, 2]
y = [3, 4]

x.extend(y)
print(x)

Output:
[1, 2, 3, 4]
""",
    },
}


def explain(sstring):
    topic = sstring

    print("\n\nDefinition:")
    print(lessons[topic]["definition"])

    print("\nSyntax:")
    print(lessons[topic]["syntax"])

    print("\nExample:")
    print(lessons[topic]["example"])


exit = False

while True:
    el = int(input("Enter the size of the list : "))
    for i in range(el):
        a = input("Enter object no. {} to add to the list : ".format(i))
        ils.append(a)
    print(ils)
    ils_archive = ils.copy()
    while True:
        fun = int(
            input(
                "Let's learn methods of List in Python !!! \n 1. append()\n 2. remove()\n 3. insert()\n 4. pop()\n 5. clear() \n 6. sort()\n 7. reverse()\n 8. count()\n 9. index()\n 10.extend() \nSelect (1,2,3....etc) : "
            )
        )
        if fun == 1:
            explain("append")
            trie = input("Enter y to try it yourself !!! : ")
            if trie.lower() == "y":
                print("Current list = ", ils)
                obj = input("Enter element to append: ")
                ils.append(obj)
                print("The intial list was : \n", ils_archive)
                print("The updated list is : \n", ils)
        elif fun == 2:
            explain("remove")
            trie = input("Enter y to try it yourself !!! : ")
            if trie.lower() == "y":
                print("Current list = ", ils)
                obj = input("Enter element to be removed: ")
                if obj in ils:
                    ils.remove(obj)
                    print("The initial list was : \n", ils_archive)
                    print("The updated list is : \n", ils)
                else:
                    print("Object not found !!!")
        elif fun == 3:
            explain("insert")
            trie = input("Enter y to try it yourself !!! : ")
            if trie.lower() == "y":
                print("Current list = ", ils)
                ind = int(input("Enter the index : "))
                obj = input("Enter element to be added: ")
                ils.insert(ind, obj)
                print("The intial list was : \n", ils_archive)
                print("The updated list is : \n", ils)

        elif fun == 4:
            explain("pop")
            trie = input("Enter y to try it yourself !!!: ")
            if trie.lower() == "y":
                print("Current list = ", ils)
                ind = int(
                    input("Enter the index of the element to pop from the list : ")
                )
                ils.pop(ind)
                print("The intial list was : \n", ils_archive)
                print("The updated list is : \n", ils)
        elif fun == 5:
            explain("clear")
            trie = input("Enter y to try it yourself !!!: ")
            if trie.lower() == "y":
                print("Current list = ", ils)
                ils.clear()
                print("The intial list was : \n", ils_archive)
                print("The updated list is : \n", ils)
        elif fun == 6:
            explain("sort")
            trie = input("Enter y to try it yourself !!!: ")
            if trie.lower() == "y":
                print("Current list = ", ils)
                ils.sort()
                print("The intial list was : \n", ils_archive)
                print("The updated list is : \n", ils)
        elif fun == 7:
            explain("reverse")
            trie = input("Enter y to try it yourself !!!: ")
            if trie.lower() == "y":
                print("Current list = ", ils)
                ils.reverse()
                print("The intial list was : \n", ils_archive)
                print("The updated list is : \n", ils)
        elif fun == 8:
            explain("count")
            trie = input("Enter y to try it yourself !!!: ")
            if trie.lower() == "y":
                print("Current list = ", ils)
                obj = input("Enter the object to be counted : ")
                print("The intial list was : \n", ils_archive)
                print("The number of occurence is : \n", ils.count(obj))
        elif fun == 9:
            explain("index")
            trie = input("Enter y to try it yourself !!!: ")
            if trie.lower() == "y":
                print("Current list = ", ils)
                obj = input("Enter the object to find its index : ")
                print("The intial list was : \n", ils_archive)
                print("The index of object is : \n", ils.index(obj))
        elif fun == 10:
            explain("extend")
            trie = input("Enter y to try it yourself !!!: ")
            if trie.lower() == "y":
                print("Current list = ", ils)
                obj = input("Enter elements separated by spaces : ")
                new_list = obj.split()

                ils.extend(new_list)

                print("The initial list was :\n", ils_archive)
                print("The updated list is :\n", ils)
        else:
            print("Invalid input !!!!")

        ex = int(input("Enter 1 to continue and 0 to exit : "))

        if ex == 1:
            continue
        elif ex == 0:
            print("Program exited succesfully!!!")
            exit = True
            break
        else:
            print("Enter valid input")
            continue
    if exit:
        break
