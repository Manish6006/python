smallest_number=0

for number in [99,100,101,1,105,11,5]:
    if smallest_number==0:
        smallest_number=number
    if number<smallest_number:
        smallest_number=number
print(smallest_number)