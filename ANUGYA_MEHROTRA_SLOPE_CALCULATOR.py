# ANUGYA MEHROTRA - 2025

# DATE CREATED: 10/10/23
# DATE MODIFIED: 4/16/25 - GITHUB LINKING



# SLOPE CALCULATOR



# Instructions for user

print("# Slope Calculator - To use this, provide your values of y1, y2, x1, x2 in the specific inputs.")
print("# Format:(x1, y1), (x2, y2)")


# Variable declaration and gather of points in slope
x1 = int(input("What is the value of x1 in your points: ")) 
print("  ")
y1 = int(input("What is the value of y1 in your points: ")) 
print("  ")
x2 = int(input("What is the value of x2 in your points: ")) 
print("  ")
y2 = int(input("What is the value of y2 in your points: ")) 

print("Output:", (x1, y1), (x2, y2))


# The calculations for slope
deltay = y2-y1
deltax = x2-x1

m = deltay/deltax

# Printing the slope
print("Slope:", m)


# Additional information for user; helpful for identifying positive or negative slopes
if int(m) in range(0, -1000):
  print("You have a negative slope.")
elif int(m) in range(0, 1000):
  print("You have a positive slope.")

