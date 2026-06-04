def is_strong(password: str) -> bool:
    if (
        len(password) < 8 or password.islower()
    ):  # Too short or there is no capital letter
        return False
    if any(char.isdigit() for char in password):  # There are numbers and letters
        return True
    return False


def main():
    print("Welcome to Password-Checker!")
    password = input("Enter your password:")
    password_strength = "strong" if is_strong(password) else "weak"
    print(f"Your password is {password_strength}.")


if __name__ == "__main__":
    main()
