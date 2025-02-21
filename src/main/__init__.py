def main(number_one: int, number_two: int) -> int:
    add = add(number_one, number_two) # it adds two numbers
    diff = number_one - number_two 
    return add, diff


def add(number_one: int, number_two) -> int:
    return number_one + number_two