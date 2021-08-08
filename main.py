import os
import sys


def power_squared(x):
    return x * x


if __name__ == '__main__':
    print(f"Process ID = {os.getpid()}")
    print(f"Python Version = {sys.version[0]}.{sys.version[2]}.{sys.version[4]}")
    print(f"Square of number {7} = {power_squared(7)}")
