def car(manufacter:str , model:str, **kwargs:str) -> str:
    always = (f"{manufacter} {model}")
    if kwargs:
        for i in kwargs.items():
            always += (f" {i[0]} {i[1]}")
    return always

print(f"{car('Alfaromeo','Giulietta', color='red')}")