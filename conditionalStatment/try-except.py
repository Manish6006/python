temp = "5 degrees"
cel = 0
print(type(temp))
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
except:
    print("not able to convert")
print(cel)