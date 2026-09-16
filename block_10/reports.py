def generate_resume(datos):
    new_dict = {
        "amount": len(datos),
        "total": sum(datos),
        "average": sum(datos) / len(datos),
        "max": max(datos),
        "min": min(datos)
    }

    return new_dict


def show_resume(resume):
    print(f"""
Amount: {resume["amount"]}
Total: {resume["total"]}
Average: {resume["average"]}
Max: {resume["max"]}
Min: {resume["min"]}
""")


def main():
    datos = [12, 56, 3.5, 24, 1]
    resume = generate_resume(datos)
    show_resume(resume)


if __name__ == "__main__":
    main()