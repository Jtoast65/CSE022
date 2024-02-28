def updatePassword(filename, website, password):
    f = open("credentials.csv", "r")
    lines = f.readlines()
    f.close()


    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split(",")
    

    for i in lines:
        if website == i[0]:
            i[2] = password

    data = ""
    counter = 0

    for i in lines:
        for x in i:
            data += str(x)
            counter += 1
            if counter == 3 and i != lines[len(lines) - 1]:
                counter = 0
                data += '\n'
            elif i != lines[len(lines - 1)]:
                data += ","
            elif counter != 3:
                date += ","

    f = open("credentials.csv", "w")
    write = f.writelines(data)
    f.close() 
updatePassword("credentials.csv", "Netflix", "abc123")
