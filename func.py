def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    print()
    description(name, age, gender)
    
def description(name, age, gender):
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Gender: {gender}")

main()