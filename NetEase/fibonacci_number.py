"""
问题描述：在Fibonacci数列中的数我们称为Fibonacci数。给你一个N，你想让其变为一个Fibonacci数，
          每一步你可以把当前数字X变为X-1或者X+1，现在给你一个数N求最少需要多少步可以变为Fibonacci数。
0,1,1,2,3,5,8...
假设n=7, 循环会在fibonaci数为8时退出，因此需要比较当前fibonacci数8和前一fibonacci数5与N之间的距离。
"""
def solution(N):
    if N == 0:
        return 0
    fib_minus_two, fib_minus_one = 0, 1
    fib = 0
    while N > fib:
        fib = fib_minus_two + fib_minus_one
        fib_minus_two = fib_minus_one
        fib_minus_one = fib
    left = abs(N - fib)
    right = abs(fib_minus_two - N)
    return min(left, right)

N = int(raw_input())
print solution(N)
