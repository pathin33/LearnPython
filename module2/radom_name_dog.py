import random
try:
    print("Ramdom name dogs!")
    with open("module2/name_dogs.txt",mode = "r") as file:
        data = file.read()
        listName = data.split('\n')
        print(f"Name : {random.choice(listName)}")
except Exception as err:
    print(err)