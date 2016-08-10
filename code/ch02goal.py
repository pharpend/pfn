'''
Take string via input(), reverse the string. Then do the same thing
again, unless the input is 'exit', in which case, exit.
'''

# We're going to exit at some point, so this is okay
while True:
    line_input = input('Enter your line: ')
    if line_input == 'exit':
        exit()
    else:
        print('Reversed line is: ' + line_input[::-1])
