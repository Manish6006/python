try:
    aInt=int(input('enter the integer value\n'))
    print(aInt&2,type(aInt))
except:
    print('terminate Abnormally')

print('Finished')

a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b  # Binary: 0001 (decimal: 1)
print(result)  # Output: 1

a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a | b  # Binary: 0111 (decimal: 7)
print(result)  # Output: 7

a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a ^ b  # Binary: 0110 (decimal: 6)
print(result)  # Output: 6

a = 5  # Binary: 0101
result = ~a  # Binary: 1010 (decimal: -6, since ~a is equivalent to -(a + 1))
print(result)  # Output: -6
