from customs import *

import sys
import math
import random
from pprint import pprint

def main() -> int:
    a = input("How old are you? ")
    if a == "":
        eprint("You didn't enter anything!")
        return 1
    a = uint8(int(a))
    print(f"You are {a} years old!")
    return 0

if __name__ == "__main__":
    code: int = main()
    if not code == 0:
        eprint(f"Program exited with code", code)
    sys.exit(code)

