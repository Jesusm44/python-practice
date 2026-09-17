import pacient

def main():
    try:
        pacients = pacient.create_user()
        print(pacient.days_since(pacients))
        pacient.future_date(pacients)
    except ValueError as error:
        print(error)


if __name__=="__main__":
    main()