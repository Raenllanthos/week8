# Maximum Multiples
# Given a divisor and a bound, find the largest integer N such that:
# N is divisible by the divisor
# N is less than or equal to bound
# N is greater than 0
# Example Input: solution(2,7)
# Example Output: 6
# Example Input: solution(3,12)
# Example Output: 12

def divide(d, b):
    return b if b%d == 0 else (b//d * d)
    # result = b//d
    # mod = b % d
    # if mod == 0:
    #     return f"Highest Dividend {b}, mod: {mod}"
    # elif result > 0:
    #      return f"Highest Dividend {result * d}, mod: {mod}"

print(divide(4, 7))
print(divide(3,12))