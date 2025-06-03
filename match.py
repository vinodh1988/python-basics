# Python 3.10+ required for match-case
code=int(input("Enter HTTP status code: "))

match code:
    case 400:
            result = "Bad request"
    case 404:
            result = "Not found"
    case 418:
            result = "I'm a teapot"
    case _:
            result = "Something's wrong with the internet"

print(f"{code}: {result}")

