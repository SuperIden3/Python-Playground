from customs import *

import sys
import math
import random
from pprint import pprint

def main() -> int:
    a = UInt8()
    a = UInt8(int(input("How old are you? ")))
    print(f"You are {a} years old!")
    return 0

if __name__ == "__main__":
    code: int = main()
    if not code == 0:
        print(f"Program exited with code {code}.", file=sys.stderr)
    sys.exit(code)

