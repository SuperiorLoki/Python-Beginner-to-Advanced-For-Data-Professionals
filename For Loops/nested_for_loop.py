products = ["iPhone", "iPad", "Macbook"]
regions = ["USA", "China", "India"]
revenue = [20,23,45,18,17,12,12,9,5]

x = 0
print("Revenue List According to Region and Product")
for product in products:
    for region in regions:
        print(f"{product} sold in {region}: {revenue[x]}")
        x+=1


for i in range(5):
    print(i)
#When you do else with a for, it will execute when the for loop is complete
else:
    print("For loop is terminated")