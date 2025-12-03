import re
import os
import sys

sys.set_int_max_str_digits(0)

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class Math:
    @staticmethod
    def avg(nums: list[float]) -> float:
        return sum(nums) / len(nums) if nums else 0.0

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
    @staticmethod
    def power(a, b):
        return a ** b
    
    @staticmethod
    def modulus(a, b):
        return a % b
    
    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def tetrate(a, b):
        if b < 1:
            raise ValueError("Tetration exponent must be at least 1.")
        result = a
        for _ in range(1, b):
            result = a ** result
        return result
    
    @staticmethod
    def pentate(a, b):
        if b < 1:
            raise ValueError("Tetration exponent must be at least 1.")
        result = a
        for _ in range(1, b):
            result = Math.tetrate(a, result)
        return result

running = True
while running:
    try:
        user_input = re.sub(" ", "", input("MaTh!!!!: ").strip().lower())
        if user_input == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        # factorial
        if user_input.endswith("!"):
            try:
                number = int(user_input[:-1])
                if not number.is_integer():
                    raise ValueError("Factorial requires a whole number.")
                result = Math.factorial(int(number))
                print(f"Result: {result}")
            except ValueError as e:
                print(e)
            continue

        # allow decimals
        match = re.match(r"(-?\d+(?:\.\d+)?)(\^\^\^|\^\^|[+\-*/%^])(-?\d+(?:\.\d+)?)", user_input)
        if match:
            num1 = float(match.group(1))
            operator = match.group(2)
            num2 = float(match.group(3))

            try:
                match operator:
                    case "+":
                        result = Math.add(num1, num2)
                    case "-":
                        result = Math.subtract(num1, num2)
                    case "*":
                        result = Math.multiply(num1, num2)
                    case "/":
                        result = Math.divide(num1, num2)
                    case "^":
                        result = Math.power(num1, num2)
                    case "%":
                        result = Math.modulus(num1, num2)
                    case "^^":
                        # tetration requires integers
                        if not num1.is_integer() or not num2.is_integer():
                            raise ValueError("Tetration requires whole numbers.")
                        result = Math.tetrate(int(num1), int(num2))
                    case "^^^":
                        # pentation requires integers
                        if not num1.is_integer() or not num2.is_integer():
                            raise ValueError("Pentation requires whole numbers.")
                        result = Math.pentate(int(num1), int(num2))
                    case _:
                        raise ValueError("Unsupported operator.")

                if result.is_integer():
                    result = int(result)
                print(f"Result: {result}")
            except ValueError as e:
                print(e)

    except KeyboardInterrupt:
        running = False
        print("\nExiting...")