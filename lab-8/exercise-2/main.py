def queryContacts(filename, areaCode):
    f = open(filename, "r")
    contacts = f.readlines()
    f.close()

    for i in range(len(contacts)):
        contacts[i] = contacts[i].strip()
    names = []

    for line in contacts:
        parts = line.split(",")
        name = parts[0]
        area = parts[1].split("-")
        code = area[0]

   
        if str(areaCode) in code:
            names.append(name)
    return names

x = queryContacts("contacts.csv", 209)
print(x)
