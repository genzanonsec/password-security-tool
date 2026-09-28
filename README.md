# Password Security Tool

I got tired of just reading about password security, so I decided to build a small tool and see what actually happens to a password when you throw it into a hashing function.

The basic idea is simple:

**Password goes in → gets salted and hashed → password goes away → hash stays.**

No passwords are sitting around in plain text looking for trouble.

## What it does

The tool currently:

* Checks basic password strength
* Generates a random salt
* Hashes passwords using PBKDF2-HMAC-SHA256
* Uses 100,000 iterations
* Verifies passwords
* Rejects incorrect passwords
* Keeps password input hidden while typing

Basically, it takes a password and makes it look like complete nonsense.

Which is exactly what we want.

## Password Strength

The tool checks for:

* At least 12 characters
* Lowercase letters
* Uppercase letters
* Numbers
* Special characters

It then gives the password a basic rating:

```text
Weak
Moderate
Strong
```

This is a simple educational check, not some magical password-strength oracle.

## Hashing

The project uses:

```text
PBKDF2-HMAC-SHA256
```

A random 16-byte salt is generated for each password.

The salt means that two identical passwords will not automatically produce identical hashes.

For example, if two people both decide that their password should be `password123`, the hashing process still gives them different results because each password gets its own salt.

Which is good, because `password123` was already a questionable decision.

## Password Verification

The tool does not need to know the original password again.

Instead, when a password is entered for verification, it:

1. Uses the same salt
2. Hashes the new password
3. Compares the new hash with the stored hash
4. Accepts or rejects it

Correct password:

```text
[+] Password verification successful.
```

Wrong password:

```text
[-] Password verification failed.
```

So yes, I tested both.

The wrong password was, in fact, wrong.

## Running It

From the project directory:

```bash
python3 password_tool.py
```

The password input is hidden in the terminal while typing.

Use fake passwords when testing this project. There is absolutely no reason to give a learning project your actual passwords.

## Project Structure

```text
password-security-tool/
├── password_tool.py
├── README.md
└── .gitignore
```

## What I Learned

This project gave me some hands-on practice with:

* Password hashing
* Salting
* PBKDF2
* Hash verification
* Secure comparisons
* Password strength checking
* `hashlib`
* `secrets`
* `getpass`

It was also a good reminder that password security is a lot more complicated than:

```text
password = "password123"
```

Please don't do that.

## Why I Built This

I wanted to understand password hashing by actually building something instead of just memorizing definitions.

Building the tool made the process much easier to understand because I could see the salt, hash, verification process, and failed login attempt happening in real time.

## Security Note

This is an educational project and is not intended to replace production password-storage systems.

Real applications should use established password-hashing libraries and follow current security recommendations.

## What's Next?

Some things I'd like to add:

* Password generator
* Better password-strength analysis
* Automated tests
* Configurable hashing settings
* Command-line options
* More detailed security reporting

For now, the password has been successfully turned into a bunch of characters that look like they know what they're doing.
