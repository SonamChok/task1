def sum_of_digits(n):
    if n < 10:      # Base case: If n is a single-digits number, return n
        return n
    
    else:           #Recursive case: Calculate the sum of digits
        last_digits = n % 10    #Get the last digits of n
        remaining_digits = n // 10  #Get the reaining digits by integer division with 10
    
        return last_digits + sum_of_digits(remaining_digits)  #Recursively call the function with the remaining digits and add the last digit to the result
   
   
print(sum_of_digits(123))
    