import re
def validate_f_name(f_name):
    while True:
        if re.match(r'^[A-Za-z]{2,}$', f_name):
            return True, f_name
        return False, "Invalid first name."

def validate_l_name(l_name):
    while True:
        if re.match(r'^[A-Za-z]{2,}$', l_name):
            return True, l_name
        return False, "Invalid last name."

def validate_password(password):
    while True:
        if re.match(r'^[A-Za-z0-9@#$%^&+=]{6,}$', password):
            return True, password
        return False, "Invalid password."

def validate_age(age):
    while True:
        if re.match(r'^[1-9][0-9]*$', age) and int(age) > 0:
            return True, age
        return False, "Invalid age."

def validate_username(username):
    while True:
        if re.match(r'^[A-Za-z0-9_]{3,}$', username):
            return True, username
        return False, "Invalid username."
