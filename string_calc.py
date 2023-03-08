import re


class StringCalculator:
    def __init__(self):
        self.delimiter = ","
        self.regex = r",|\n"

    def add(self, numbers):
        if not numbers:
            return 0

        # Check for consecutive delimiters
        if re.search(',\n', numbers):
            raise ValueError("invalid input")

        # Check for custom delimiter
        match = re.match(r"//(.*)\n(.*)", numbers)
        if match:
            self.delimiter = match.group(1)
            self.regex = "|".join([re.escape(d) for d in self.delimiter])
            numbers = match.group(2)

        # Split the input string using the delimiter regex
        nums = re.split(self.regex, numbers)

        # Calculate the sum of the numbers
        negatives = []
        total = 0
        for n in nums:
            if n:
                try:
                    n = int(n)
                    if n < 0:
                        negatives.append(n)
                    elif n <= 1000:
                        total += n
                except ValueError:
                    raise ValueError("invalid input")

        # Handle negative numbers
        if negatives:
            msg = "negatives not allowed: " + ",".join(map(str, negatives))
            raise ValueError(msg)

        return total

if __name__ == "__main__":
    sc = StringCalculator()
    numbers = input("Number: ")
    total = sc.add(numbers)
    print(total, '!!!!!!')