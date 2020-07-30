# # Francesco Lopez - 11/03/2018 - Assignment: PasswordChecker2

# PSEUDOCODE

# MIN_PASS_LENGTH
# MAX_PASS_LENGTH

# INPUT = password
# pass_length

# WHILE pass_length < MIN_PASS_LENGTH or pass_length > MAX_PASS_LENGTH
#   OUTPUT = error
#   INPUT = password
#   pass_length ENDWHILE

# IF password is numeric THEN
#   OUTPUT = weak password, pass length

# ELSE password is alpha THEN
#   OUTPUT = weak password, pass length

# ELSE password is alphanumeric THEN
#   OUTPUT = strong password, pass length

# ELSE password contains special characters THEN
#   OUTPUT = strong password, pass length
# ENDIF

# END


MIN_PASS_LENGTH = 6
MAX_PASS_LENGTH = 14

print('PasswordChecker2 program developed by: Francesco Lopez')

password = input('Please enter a password:')

pass_length = len(password)

# If password <6 or >14 loop is activated.
while pass_length < MIN_PASS_LENGTH or pass_length > MAX_PASS_LENGTH:
    print('Password not valid.')
    password = input('Please enter a password containing min. of 6 or max. of 14 characters:')
    pass_length = len(password)
    # pass_length to recalculate new input to be able to exit from the loop if loop is false.

if password.isnumeric():
    print('Weak password. It contains only numbers, consider a combination of number and letters.'
          f'\nYour password is {pass_length} characters long')
elif password.isalpha():
    print('Weak password. It contains only letters, consider a combination of number and letters.'
          f'\nYour password is {pass_length} characters long')
elif password.isalnum():
    print(f'Your password is strong, it contains a combination of numbers and letters.' 
          f'\nPassword is {pass_length} character long.')
else:
    print(f'Your password is strong, it contains a combination of numbers/letters or special characters' 
          f'\nPassword is {pass_length} character long.')

