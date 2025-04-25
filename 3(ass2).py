def count_divisible_positions(N):
    count = 0
    str_N = str(N)  
    for digit in str_N:
        if digit != '0': 
            if N % int(digit) == 0:
                count += 1

    return count

t = int(input("Enter number of test cases: "))

if 1 <= t <= 15:
    results = []
    for _ in range(t):
        N = int(input())  
        if 0 <= N <= 10**10:  
            results.append(count_divisible_positions(N))
    for res in results:
        print(res)