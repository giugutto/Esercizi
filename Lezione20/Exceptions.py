import math
    
#1 Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). Handle ValueError if the input is negative by returning an informative message.
def safe_sqrt(number):
    try:
        return math.sqrt(number)
    except ValueError:
        return "Numero negativo"

print(safe_sqrt(0))
print(safe_sqrt(4))
print(safe_sqrt(-8))

    #2 Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.



def validate_password(password):
    
    lunghezza = 0
    maiuscolo = 0
    specialicounter = 0
        
    for i in password:
        lunghezza += 1
        

    v_lista: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
    while maiuscolo < 3:
        for i in v_lista:
            if i in password:
                maiuscolo += 1
            else:
                continue
        
        
    special: list = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',  ']', '_', '`', '{', '|', '}', '~']
    
    for i in special:
        if i in password:
            specialicounter += 1
        if specialicounter == 4:
            break
            
        

    
    if lunghezza < 20:
        raise ValueError("La password deve essere lunga ale")
    elif maiuscolo < 3:
        raise ValueError("La password deve contenere almeno 3 lettere maiuscole")
    elif specialicounter < 4:
        raise ValueError("La password deve contenere almeno 4 caratteri speciali")
    else:
        return "La password è valida"
    
class InvalidPasswordError(Exception):
    pass


print(validate_password("ksfnjsiopfJsoimjfsmdfSmfdk"))



    #3 Context Managers for File Handling: Use the with statement and context managers to open and close a file. Handle potential IOError within the with block for clean resource management.

    #4 Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.  A query on a given date allows for retrieving a given new date. Note that a date is an object for your database; it must be instantiated from a string.

    #5 An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying to (possibly) cover all execution paths! User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
    #      If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
    #     Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError.
    #     If the second input is not '+' or '-', again raise a FormulaError.
    #     If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

    #6 Personalized math library: Create a Python library that provides functions for handling fractions, with built-in error handling. The library must include functions for the following operations:
    #     Create a fraction from the numerator and denominator.
    #     Collect the numerator and denominator of a fraction.
    #     Simplify a fraction.
    #     Add, subtract, multiply and divide fractions.
    #     Check whether one fraction is equivalent to another. 

    #     All library functions must use the try-except block to handle potential errors, such as null denominators, unsupported operations, or division by zero. The library must raise custom exceptions to indicate specific errors to the user.


    #7  Custom Exception for Data Structure Integrity: Define a custom exception class DataStructureIntegrityError.  Define the custom data structure linked list use classes with methods to append, remove and access a given element, and write functions that operate on that (i.e., print the list,  reverse the list, and check whether the list is ordered). Raise this exception if the data structure's integrity is compromised (e.g., empty list access, index error).
