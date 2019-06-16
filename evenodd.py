
'''''''''''''' EVEN _ ODD FUNTTION ''''''''''''''

''''''''''''''TAKES SOMETHING RETURN SOMETHING '''''''


val1 = int(input("enter val 1:"))
def even_odd(val1):               # function definition with arguments
    if val1 % 2 == 0:             # condition for even
        ans = "even"
        return ans                
    else:                         # else for odd
        ans = "odd"
        return ans 
output_of_function = even_odd(val1) 
print(output_of_function)