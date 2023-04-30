import string
import random


class SkuGeneratorUtil:
    @staticmethod
    def generate_sku():
        size = 8
        chars = string.ascii_uppercase+string.digits

        return "".join(random.choice(chars) for _ in range(size))

