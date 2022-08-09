'''
Break command is used to break the loop condition
'''

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))


print('Done')