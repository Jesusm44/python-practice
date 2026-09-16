import os

def read_file():
    filename= "file_notes.txt"
    if not os.path.exists(filename):
        raise FileNotFoundError("The file does not exist.")
    file = open(filename, "r")

    content = file.read()
    print(content)
    file.close()