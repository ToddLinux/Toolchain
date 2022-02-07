#!/usr/bin/env python3
from check_req import *
import sys

if __name__ == "__main__":
    if not check_all_requirements():
        print("Nay")
        sys.exit(1)

    print("Yay")