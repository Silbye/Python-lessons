import os
os.system('cls')

def export_data(data, separate):
    with open('lesson7/phones.csv', 'a+') as file:
        if separate == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(separate.join(data))
            file.write(f"\n")

def import_data():
    with open('lesson7/phones.csv', 'r') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data