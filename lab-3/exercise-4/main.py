grade = int(input())

if grade in range(90,101):
    print (f'A')
elif grade in range(80,90):
    print (f'B')
elif grade in range(70,80):
    print (f'C')
elif grade in range(60,70):
    print (f'D')
elif grade in range (0,60):
    print (f'F')
else:
    print (f'Invalid mark.')