import string
import getpass


def check_password_strength(password: str) -> int:
    score = 0
    if len(password) >= 8:  # Too short or there is no capital letter
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):  # There are numbers and letters
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    special_chars = set(string.punctuation)
    if any(char in special_chars for char in password):
        score += 1
    return score


def main():
    print("Welcome to Password-Checker!")
    password = getpass.getpass("Enter your password:")
    strength_levels = [
        "Super Weak 🥶",
        "Very Weak ⚠️",
        "Weak 👎🏽",
        "Medium 👍🏽",
        "Strong 💪🏽",
        "Very Strong 🔥",
    ]
    strength_level = strength_levels[check_password_strength(password)]
    print(f"Strenth Level: {strength_level}")


if __name__ == "__main__":
    main()
