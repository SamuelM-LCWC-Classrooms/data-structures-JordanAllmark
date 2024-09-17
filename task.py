def task_1(): # Lists (done)

    origional_list = ["Geoff", "Jeff", "Jeffrey"]
    name = input("Enter your name: ")
    origional_list.insert(0, name)
    origional_list.pop(1)
    new_list = origional_list.copy()

    return new_list

    


def task_2(): # Dictionaries

    keys = ("name", "age", "profession")
    values = ("Geoff", 35, "technician")
    person = dict(zip(keys, values))

    car = {
        "make": "Ford",
        "model": "Focus",
        "engine": 1.6,
        "colour": "blue"
    }

    person.append(car)

    return person


def task_3(): # Tuples
    student_1 = ("Geoff", "Maths", 80)
    student_2 = ()

    student_list = list(student_2)
    name = str(input("Enter your Name: "))
    subject = str(input("Enter your Subject: "))
    score = int(input("Enter your Score out of 100: "))
    student_list.append(name)
    student_list.append(subject)
    student_list.append(score)
    student_2 = tuple(student_list)

    return students


def task_4(): # Sets
    fruits_1 = {"apple", "banana", "cherry", "grape", "mango", "pineapple", "papaya","sprite", "orange", "lemon", "strawberry"}
    fruits_2 = {"raspberry", "banana", "cherry", "grape", "mango", "blueberry", "papaya", "melon", "lemon", "steak"}

    duplicate_fruits = None # This should be a tuple containing all the fruits in both tuples
    individual_fruits = None # This should be a tuple containing only the individual fruits


    return [duplicate_fruits, individual_fruits] # Note - functions can only return one data item - so both tuples
                                                 # are contained inside a single list
print(task_3())