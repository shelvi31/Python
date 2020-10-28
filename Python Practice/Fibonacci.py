def Fibonacci(n):
    sequence = [1,1,2]
    for i in range(3,n+1):
        sequence.append(sequence[i-1]+ sequence[i-2])
    return sequence

print(Fibonacci(80))
