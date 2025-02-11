def password(code):
    if len(code) > 8:
        return False
    elif not any(char.isdigit() for char in code):
        return False
    elif not any(char.islower() for char in code):
        return False
    elif not any(char.isupper() for char in code):
        return False
    elif not any(char in '@+_*&^()#)' for char in code):
        return False
    else:
        return True

print(password('Gaja@123'))  
print(password('Hello'))    

