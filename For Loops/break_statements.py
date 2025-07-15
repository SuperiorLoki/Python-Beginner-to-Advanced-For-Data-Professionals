monthly_sales = [42,38,33,38,40,45, 29, 28]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]

threshold = 35

'''
for i, sales in enumerate(monthly_sales):
    if sales < threshold:
        print(f"Sales amount, {sales}, is less than threshold which happened on {months[i]}")
OR
'''

#The Zip function will allow us to combine both basically for the sake of the for loop
for sales, month in zip(monthly_sales, months):
    #The Zip function will go up to the lower length list
    print(f"The sales in the {month} month was {sales}")


