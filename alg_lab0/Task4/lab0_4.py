import time
start_time = time.perf_counter()

fib1 = fib2 = 1
num = open("Task4/input.txt").read()
n = int(num)
if 0<n<45:
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    open('Task4/output.txt', 'w').write(str(fib2))
else:   
    print("The numbers are too big!")
print(time.perf_counter() - start_time)

finish_time = time.perf_counter()
print('Time: ' + str(finish_time - start_time))


start_time = time.perf_counter()
fib1 = fib2 = 1
num = open("Task4/input1.txt").read()
n = int(num)
if 0<n<10**7:
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2

    open('Task4/output1.txt', 'w').write(str(fib2%10))

else: 
    print("The numbers are too big!")
finish_time = time.perf_counter()
print('Time: ' + str(finish_time - start_time))

