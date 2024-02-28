def areaOfCircle(radius):
   area = 3.14159 * (radius**2)
   area = float(f'{area:.2f}')
   return area

a = areaOfCircle(3)
print(a)