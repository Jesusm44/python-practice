from storage import read_file

def main():
    try:
        read_file()
    except FileNotFoundError as error:
        print(error)


if __name__=="__main__":
    main()