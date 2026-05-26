import random
import string

class PasswordGeneration:

    @staticmethod
    def generate():
        # string.ascii_letters = a-z and A-Z
        # string.digits = 0-9
        # string.punctuation = symbols like !#$%&()*+


        letters = [random.choice(string.ascii_letters) for _ in range(8)]
        digits = [random.choice(string.digits) for _ in range(2)]
        punctuation = [random.choice(string.punctuation) for _ in range(2)]

        password_list = letters + digits + punctuation

        random.shuffle(password_list)
        return "".join(password_list)