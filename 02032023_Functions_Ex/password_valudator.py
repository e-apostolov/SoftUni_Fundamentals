def validate_password(password):
    is_password_valid = True
    if len(password) < 6 or len(password) > 10:
        is_password_valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        is_password_valid = False
        print("Password must consist only of letters and digits")
    counter_of_digits = 0
    for character in password:
        if character.isdigit():
            counter_of_digits += 1
    if counter_of_digits <2:
        is_password_valid = False
        print("Password must have at least 2 digits")
    return is_password_valid

password_input = input()
is_valid = validate_password(password_input)
if is_valid:
    print("Password is valid")
