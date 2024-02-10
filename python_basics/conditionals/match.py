'''match statements can be used to conditionally run code that matches certain values'''

name = input("What's your name?").strip().capitalize() 
match name:
    case "Harry":
        print('01')
    case "Hermione":
        print('01')
    case "Dracko":
        print("02")
    case "Drake":
        print("02")
    case "Apple" | "Orange" | "Guava":
        print("Fruit")
    case _:
        print("Who?")