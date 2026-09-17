from json import JSONDecodeError

import patient
import output
import storage
import input

def main() -> None:
    patients = storage.load_patients()

    run_program = True
    while run_program:
        output.options()
        options= input.options()

        if options == 1:
            try:
                new_patient = patient.create_patient()
                patients.append(new_patient)
                print("Patient created")
            except ValueError as error:
                print(error)
        elif options == 2:
            storage.save_patient(patients)
        elif options == 3:
            try:
                patients = storage.load_patients()
                print(patients)
            except JSONDecodeError:
                print("ERROR IN JSON")
            except TypeError as error:
                print(error)
        elif options == 4:
            try:
                patient.delete_pacient(patients)
                storage.save_patient(patients)
            except ValueError as error:
                print(error)
        elif options == 5:
            print("Exit the program...")
            run_program = False
        else:
            print("Invalid option")
        

if __name__ == "__main__":
    main()

