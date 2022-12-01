def password_validator(secret):
    character_counter = 0

    if len(secret) < 6 or len(secret) > 10:
        print("Password must be between 6 and 10 characters")
    if not secret.isalnum():
        print("Password must consist only of letters and digits")
    for character in secret:
        if character.isdigit():
            character_counter += 1
    if character_counter < 2:
        print("Password must have at least 2 digits")
    if 6 <= len(secret) <= 10 and secret.isalnum() and character_counter >= 2:
        print("Password is valid")


password = input()
password_validator(password)