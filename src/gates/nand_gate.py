from src.gates.and_gate import and_gate

def nand_gate(x:bool, y:bool) -> bool:
    return not and_gate(x, y)