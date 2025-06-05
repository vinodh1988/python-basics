from ownException import InvalidIdError

def readPerson():
    try:
        sno = int(input("Enter sno: "))
        name = input("Enter name: ")
        city = input("Enter city: ")
      
        if sno <= 0:
            raise InvalidIdError("sno must be positive")
        print(f"sno: {sno}, name: {name}, city: {city}")
    except ValueError:
        print("Invalid input: sno must be an integer.")
    except InvalidIdError as e:
        print(f"InvalidIdError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

readPerson()