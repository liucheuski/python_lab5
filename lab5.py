fib1 = 0
fib2 = 0
fib3 = 1

n = int(input("Номер элемента ряда трибоначчи: "))

i = 0
while i < n - 3:
    fib_sum = fib1 + fib2 + fib3
    fib1 = fib2
    fib2 = fib3
    fib3 = fib_sum
    i = i + 1

print("Значение этого элемента:", fib3)
