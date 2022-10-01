def logical_and(x: bool, y: bool) -> bool:
    out = x and y
    return out

def logical_not(x: bool) -> bool:
    out = not x
    return out

def logical_nand(x: bool, y: bool) -> bool:
    x_y_and = logical_and(x, y)
    out = logical_not(x_y_and)
    return out

def logical_or(x: bool, y: bool) -> bool:
    x_not = not x
    y_not = not y
    out = logical_nand(x_not, y_not)
    return out

def logical_xor(x: bool, y: bool) -> bool:
    x_y_or = logical_or(x, y)
    x_y_nand = logical_nand(x, y)
    out = logical_and(x_y_or, x_y_nand)
    return out

def logical_adder(x: bool, y: bool, in_carry: bool = False) -> tuple[bool, bool]:
    x_y_xor = logical_xor(x, y)
    x_y_and = logical_and(x, y)
    out_sum = logical_xor(x_y_xor, in_carry)
    x_y_xor_carry_and = logical_and(x_y_xor, in_carry)
    out_carry = logical_or(x_y_and, x_y_xor_carry_and)
    return out_sum, out_carry

def logical_four_bit_adder(x: list[bool], y: list[bool], in_carry: bool = False) -> tuple[list[bool], bool]:
    sum1, carry = logical_adder(x[-1], y[-1], in_carry)
    sum2, carry = logical_adder(x[-2], y[-2], carry)
    sum3, carry = logical_adder(x[-3], y[-3], carry)
    sum4, out_carry = logical_adder(x[-4], y[-4], carry)
    return [sum4, sum3, sum2, sum1], out_carry

def invert_four_bit(x: list[bool], invert: bool):
    inv1 = logical_xor(x[-1], invert)
    inv2 = logical_xor(x[-2], invert)
    inv3 = logical_xor(x[-3], invert)
    inv4 = logical_xor(x[-4], invert)
    return [inv4, inv3, inv2, inv1]

def logical_alu(x: list[bool], y: list[bool], substract: bool = False) -> tuple[list[bool], bool, bool, bool]:
    y_xor = invert_four_bit(y, substract)
    out, carry = logical_four_bit_adder(x, y_xor, substract)
    zero = logical_and(logical_and(logical_and(logical_not(out[-1]), logical_not(out[-2])), logical_not(out[-3])), logical_not(out[-4]))
    negative = out[0]
    return out, carry, negative, zero

if __name__ == "__main__":
    print(logical_alu([True, True, True, False], [True, True, False, False], True))