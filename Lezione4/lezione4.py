# 8-1. Message: Write a function called display_message() 
#that prints one sentence telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.

def message() -> str:
    print("Hi everyone, i'm learning function in python")

message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
# The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
# Call the function, making sure to include a book title as an argument in the function call.

def favourite_book(title:str):
    x = print(f"One of my favourite books is {title}")
    return x
    
favourite_book("Il profumo")

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message
# that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

def make_shirt(size:str, text: str):
    x = print(size + text)
    return x

taglia = "S"
messaggio = " Stan"

make_shirt(taglia,messaggio)

make_shirt("XL", " ciao")

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt():
    print("L" + " I love python")

make_shirt()

def make_shirt():
    print("M" + " I love python")

make_shirt()

def make_shirt():
    print("XXL" + " port scanning is not a crime")

make_shirt()