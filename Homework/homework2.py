def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        total = fibonacci(int(n)-1)+fibonacci(int(n)-2)
        return total

print(fibonacci(input("Enter a integer: ")))
