import hashlib
import secrets
import getpass
import string


def check_password_strength(password):
    score = 0

    if len(password) >= 12:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"

    if score <= 4:
        return "Moderate"

    return "Strong"


def hash_password(password):
    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return salt, password_hash


def verify_password(password, salt, stored_hash):
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return secrets.compare_digest(password_hash, stored_hash)


def main():
    print("=" * 50)
    print("        PASSWORD SECURITY TOOL")
    print("=" * 50)
    print()

    password = getpass.getpass("Enter a password: ")

    strength = check_password_strength(password)

    print()
    print("Password strength:", strength)
    print()

    salt, password_hash = hash_password(password)

    print("[+] Password hashed successfully.")
    print()
    print("Salt:")
    print(salt.hex())
    print()
    print("Password hash:")
    print(password_hash.hex())
    print()

    print("Now let's verify the password.")
    print()

    test_password = getpass.getpass("Enter the password again: ")

    if verify_password(test_password, salt, password_hash):
        print("[+] Password verification successful.")
    else:
        print("[-] Password verification failed.")


if __name__ == "__main__":
    main()
