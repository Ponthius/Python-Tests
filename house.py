name = input("What's your name? ")

match name:
    case "Poel":
        print("PCSE")
    case "Ponthius":
        print("NCBA")
    case "George" | "Henry" | "Prena":
        print("Native")
    case _:
        print("Unknown")
