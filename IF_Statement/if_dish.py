indian = ['samosa', 'daal', 'naan']
chinese = ['egg roll', 'pot sticker', 'fried rice']
italian = ['pizza', 'pasta', 'risotto']

dish = input("Enter a dish: ")

if dish in indian:
    print(f"{dish}  is an indian cuisine")
elif dish in chinese:
    print(f"{dish}  is a chinese cuisine")
else:
    print(f"{dish}  is an italian cuisine")