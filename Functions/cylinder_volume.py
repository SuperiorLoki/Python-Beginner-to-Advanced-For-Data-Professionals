def find_cylinder_volume(radius, height=7):
    return 3.14*(radius ** 2)*height


r = int(input("What is the radius of the cylinder: "))
h = int(input("What is the height of the cylinder: "))

print(f"The volume of the cylinder is {find_cylinder_volume(r, h)}")

#Alternative way to input the input values when calling the function
print(find_cylinder_volume(height = 5, radius = 3))