import os

path = os.getcwd()  # get current working directory, i.e.the directory where we are going to read files
print("Directory path:", path)

files = os.listdir()  # get all the files in the directory

for file in files:
    print(file)
