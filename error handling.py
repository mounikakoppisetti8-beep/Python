def safe_divide(numerator,denominator):
    try:
        result = numerator / denominator
        print("The result of {numerator} / {denominator} is:{result}")
    except ZeroDivisionError:
        print("Error:Cannot divide by zero! Attempted {numerator}/{denominator}")
    except TypeError:
        print("Error: Invalid input types.Please provide numbers.")
    except Execution as e:
        print("An unexpected error occured: {e}")
        
#Demonstrating error handling
print("\n---Error Handling Demonstration---")
safe_divide(10,2)
safe_divide(10,0)
safe_divide(5,"abc")