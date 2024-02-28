def updatePassword(filename, website, password):
    f = open("credentials.csv", "r")
    creds = f.readlines()
    f.close()
    

    d = list(i.strip() for i in creds)
    creds = []

    for i in d:
        creds.extend(i.split(","))
    
    e = creds[1]

    safety = {creds[i] : creds[(i+2)] for i in range(0,(len(creds)), 3)}

    if website in safety.keys():
        safety[website] = password
    
    data = [key + ',' + e + ',' + value + '\n' for (key,value) in safety.items()]
    data[-1] = data[-1][:-1]

    f = open("credentials.csv", 'w')
    write = f.writelines(data)
    f.close()

updatePassword("credentials.csv", "Netflix", "abc123")