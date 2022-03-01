# a program that prints the prime numbers from 1 to 100
def primeNumbers():
    for i in range(2,15):
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            print(i)

primeNumbers()


times3 = 6
once = 10
twice = 4

mean = (times3 + once + twice) / 40

print(mean)