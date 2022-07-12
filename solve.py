from itertools import product
from time import time

OP = ["+", "*", "%"]


def solve(input_number: list[int]):
    p = list(map(list, product(OP, repeat=len(input_number) - 2)))
    answer = 0

    ops_list = []
    for i in p:
        for n in range(len(i) + 1):
            ops = i[::]
            ops.insert(n, "=")
            ops_list.append(ops)

    for ops in ops_list:
        numbers = input_number[::]
        sum = numbers.pop(0)
        while numbers:
            a = numbers.pop(0)
            op = ops.pop(0)

            if op == "=":
                left = sum
                sum = a
            elif op == "+":
                sum += a
            elif op == "*":
                sum *= a
            elif op == "%":
                sum %= a

        if left == sum:
            answer += 1

    return answer


if __name__ == "__main__":
    iteration = int(input())

    for _ in range(iteration):
        __ = int(input())
        input_number = list(map(int, input().split()))

        start = time()
        answer = solve(input_number)
        print(f"{answer}, time : {time() - start}")
