def welcome_message():
    print("Welcome to the Cake Cutting Program")
    print("Choose how you'd like to cut the cake:")
    print("1. Unequal Pieces")
    print("2. Equal Pieces")

def unequal_pieces(n):
    print("\nYou chose UNEQUAL pieces.")
    print("1. All pieces of different size")
    print("2. Pieces of different sizes but some may be the same")
    s = input("Enter your choice (1 or 2): ")

    if s == "1":
        if n <= 26:
            print("It is possible to cut the cake into", n, "unequal pieces of different size.")
        else:
            print("Not possible. You can have at most 26 uniquely sized pieces.")
    elif s == "2":
        if n <= 360:
            print("It is possible to cut the cake into", n, "pieces of different or repeating sizes.")
        else:
            print("Not possible. A circle (360°) can't be divided into more than 360 parts.")
    else:
        print("Invalid choice for unequal pieces.")

def equal_pieces(n):
    print("\nYou chose EQUAL pieces.")
    if 360 % n == 0:
        print("Possible to cut the cake into", n, "equal pieces. Each piece is", 360 // n, "degrees.")
    else:
        print("Not possible. 360 is not divisible evenly by", n)

def main():
    welcome_message()
    choice = input("Enter your choice (1 or 2): ")
    
    try:
        n = int(input("Enter the number of pieces you want: "))
        if n <= 0:
            print("Number of pieces must be greater than 0.")
            return

        if choice == "1":
            unequal_pieces(n)
        elif choice == "2":
            equal_pieces(n)
        else:
            print("Invalid main choice.")
    except ValueError:
        print("Please enter a valid number for the pieces.")

if __name__ == "__main__":
    main()
