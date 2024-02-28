
width = int(input())
height = int(input())

for x in range(height):
    star = "*"
    for y in range(width-1):
        if x == 0 or x == (height-1):
            star += " *"
        elif y == (width-2):
            star += " *"
        else:
            star += "  "
    print(star)