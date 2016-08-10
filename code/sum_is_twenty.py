'''
Takes two numbers. If their sum is 20, then print 'yay', otherwise
print 'boo'.
'''

first_number = input('First number: ')
first_number_as_int = int(first_number)

second_number = input('Second number: ')
second_number_as_int = int(second_number)

if first_number_as_int + second_number_as_int == 20:
    print('yay')
else:
    print('boo')
