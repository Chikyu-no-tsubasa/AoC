"""
https://adventofcode.com/2024/day/2
To compile and run:
g++ Day3_1.cpp -o Day2_1
./Day2_1
"""

import re

def parse_and_sum(path: str) -> int:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = re.compile(r"(?:do\(\))|(?:don't\(\))|mul\((\d{1,3}),(\d{1,3})\)")

    enabled = True   
    total = 0

    for m in pattern.finditer(text):
        token = m.group(0)   

        if token.startswith("do("):
            enabled = True

        elif token.startswith("don'"):
            enabled = False

        elif token.startswith("mul") and enabled:
            a = int(m.group(1))
            b = int(m.group(2))
            total += a * b
    
    return total


if __name__ == "__main__":
    
    result = parse_and_sum("input.txt")
    print(result)
