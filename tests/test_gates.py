from itertools import product
from src.gates.and_gate import and_gate

def and_gate_test():
    for x, y in product([True, False], repeat=2):
        print(f"x={x}, y={y}")
        print("Z=", end="")
        print(and_gate(x, y))


def main():
    and_gate_test()

if __name__ == "__main__":
    main()