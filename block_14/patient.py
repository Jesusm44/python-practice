import input
import validation
import datetime

def create_patient():
    register: datetime.date = datetime.date.today()
    new_register: str = register.strftime("%d/%m/%Y")

    name: str = input.name().capitalize()
    age: int = input.age()

    valid_name: str = validation.validation_name(name)
    validage: int = validation.validation_age(age)

    new_patient = {
        "name": valid_name,
        "age": validage,
        "registration" : new_register
    }

    return new_patient

def delete_pacient(patients):
    name: str = input.name().capitalize()
    validname: str = validation.validation_name(name)

    result = list(
        filter(
            lambda pacient: pacient["name"] == validname, patients
        )
    )
    if result:
        patients.remove(result[0])
        print(f"The patient {name} has been deleted.")
    else:
        raise ValueError("Patient not found")