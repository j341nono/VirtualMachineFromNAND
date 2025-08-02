from itertools import product
from typing import Callable
from src.gates.and_gate import and_gate
from src.gates.nand_gate import nand_gate
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--and_gate", action="store_true")
    parser.add_argument("--nand_gate", action="store_true")
    return parser.parse_args()

def gate_test(func: Callable[[bool, bool], bool]):
    print(f"function name: {func.__name__}")
    for x, y in product([True, False], repeat=2):
        print(f"x={x}, y={y}")
        print("Z=", end="")
        print(func(x, y))

def main():
    args = parse_args()
    if args.and_gate:
        gate_test(and_gate)
    if args.nand_gate:
        gate_test(nand_gate)

if __name__ == "__main__":
    main()