def isPowerOfFive(n):
    if n == 1:
        return True
    elif n < 1 or n % 5 != 0:
        return False
    else:
        return isPowerOfFive(n / 5)

# Example usage:
result = isPowerOfFive(125)
print(result) 