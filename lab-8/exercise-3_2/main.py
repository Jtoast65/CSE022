def updatePassword(filename, website, password):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for x in range(len(lines)):
        line = lines[x]


        if line.split(",")[0].strip() == website:
            y = line.split(",")
            y[2] = password

            if (x+1) != len(lines):
                lines[x] = (",".join(y) +'\n')
            else:
                lines[x] = (",".join(y))


    f = open(filename, "w")
    f.writelines(lines)
    f.close()

updatePassword("credentials.csv", "Netflix", "abc123")