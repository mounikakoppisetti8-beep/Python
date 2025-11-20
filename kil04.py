def kg_to_pounds():
    try:
        kilograms = float(input("Enter the weight in kilograms:"))
        pounds = kilograms*2.20462
        print(f"The weight in pounds is:{pounds:.2f}")
    expect ValueError:
        Print(f"Invakid input. please enter anumerical value for weight.")
        
        #call the function directly to run the conversion
        kg_to_pounds()
        