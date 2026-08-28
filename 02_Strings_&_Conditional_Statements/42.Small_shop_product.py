#small shop that sells products

prices = float(input("Enter the price of product per unit: "))

for i in range(1, 11):  
   
    discount = prices - (i - 1) * 0.5
    if discount < 0:  
        discount = 0
    total_cost = i * discount
    
    print(f"Units: {i}, Price per Unit: ${discount}, Total Cost: ${total_cost:}")
