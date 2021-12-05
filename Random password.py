import random
#User input from password lenght
pass_len = int(input("Enter Password Of Lenght : "))

#password variable to define some charector's and number's and special symbols
password = "qwertyuioplkjhgfdsazxcvbnm0123456789QWERTYUIOPLKJHGFDSAZXCVBNM@#$%&*()^~"

#this is the formula to generate the password
generate = "".join(random.sample(password,pass_len))

#then print
print(generate)

#Second Method
#Another wey to generate random passwords:
import random
#User input from password lenght
pass_len = int(input("Enter Password Of Lenght : "))

# use to different - different types
upperstr = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowerstr = "qwertyuioplkjhgfdsazxcvbnm"
numbers = "0123456789"
symbol = "~!@#$%^&*()_+|></"
password = upperstr+lowerstr+numbers+symbol
#this is the formula to generate the password
generate = "".join(random.sample(password,pass_len))

#then print
print(generate)
