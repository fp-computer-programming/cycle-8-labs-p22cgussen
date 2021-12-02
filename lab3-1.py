# Author CCG 12/1/21

def sum_to(n):
    i = 0
    total = 0
    while i <= n:
        total += i
        i += 1
    return total

value = input("Enter your integer: ")
print(sum_to(int(value)))