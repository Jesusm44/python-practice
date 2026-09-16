import reports


def main():
    datos = [10, 20, 30, 40]
    resume = reports.generate_resume(datos)
    print("Desde main.py:")
    reports.show_resume(resume)

if __name__ == "__main__":
    main()