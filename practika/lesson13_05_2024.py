def check_password(password):
    return len(password) >=8 and any(i.islower() for i in password) and any(i.isupper() for i in password) and any(i.isdigit() for i in password)
print(check_password('Abcd1234')) #True
print(check_password('qwerty')) #False
print(check_password('abcD')) #False
print(check_password('ABCD1234')) #False

