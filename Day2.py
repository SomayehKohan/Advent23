import re

filepath = "C:\\Users\\dateuser\\Desktop\\input2.txt"


def find_digits(word):
    line1 = word.split(':')
    #print(line1)
    line2 = line1[1].split(';')
    #print(line2)
    id = re.findall(r'\d+', line1[0])
    #print(id)
    for element in line2:
        line3 = element.split(',')
        #print(line3)
        for el in line3:
            num = re.findall(r'\d+', el)
            #print(num)
            if 'red' in el:
                if int(num[0]) > 12:
                    return 0
            elif 'green' in el:
                if int(num[0]) > 13:
                    return 0
            elif 'blue' in el:
                if int(num[0]) > 14:
                    return 0
    print("id = ", id[0])
    return id[0]

def powerOfSet(word):
    line1 = word.split(':')
    #print(line1)
    line2 = line1[1].split(';')
    #print(line2)
    id = re.findall(r'\d+', line1[0])
    numred = 0
    numblue = 0
    numgreen = 0
    for element in line2:
        line3 = element.split(',')
        #print(line3)
        for el in line3:
            num = re.findall(r'\d+', el)
            #print(num)
            if 'red' in el:
                if int(num[0]) > numred:
                    numred = int(num[0])
            elif 'green' in el:
                if int(num[0]) > numgreen:
                    numgreen = int(num[0])
            elif 'blue' in el:
                if int(num[0]) > numblue:
                    numblue = int(num[0])
    print("powercub = ", numred*numblue*numgreen)
    return numred*numblue*numgreen



if __name__ == '__main__':

    f = open(filepath, "r")
    text = f.read()
    text1 = text.splitlines()
    sum1 = 0
    for el in text1:
       print(el)
       #el2 = find_digits()
       el2 = powerOfSet(el)
       print(el2)
       sum1 += int(el2)

    print(sum1)
