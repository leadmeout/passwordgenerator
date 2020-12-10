import random
import string

password_length = int(input("How long should the password be?\n"))
numbers_count = int(input("How many numbers should your password have?\n"))
special_characters_count = int(input("How many special characters should your password have?\n"))


def password_generator(password_length, numbers_count, special_characters_count):

    password = []

    for count in range(0, numbers_count):
        password.append(random.choice(string.digits))

    for count in range(0, (password_length - numbers_count - special_characters_count)):
        password.append(random.choice(string.ascii_letters))

    for count in range(0, special_characters_count):
        password.append(random.choice(string.punctuation))

    random.shuffle(password)
    password = ''.join([str(i) for i in password])

    print(f"Your password is: {password}")

password_generator(password_length, numbers_count, special_characters_count)

