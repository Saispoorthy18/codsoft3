import random
import string

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    all_characters = lowercase + uppercase + digits + punctuation
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]

    for _ in range(length - 4):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    password = ''.join(password)

    return password

length = int(input("Enter password length (min 8): "))
print("Generated Password : ", generate_password(length))

