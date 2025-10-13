import math
def permutat(n, r):
    """Calculate the number of permutations of n items taken r at a time."""
    if r > n or n < 0 or r < 0:
        return 0
    numerator = math.factorial(n)
    denominator = math.factorial(n - r)
    return numerator // denominator
# Example usage:
n = 5   
r = 3
result = permutat(n, r)
print(f"P({n}, {r}) =", result)  # Output: P(5, 3) = 60