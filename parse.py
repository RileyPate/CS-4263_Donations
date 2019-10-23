file = open("data/pac_example.txt", "r")
text = file.read()
array = text.split('\n')
#print(array)
for x in range(0, array.__len__()):
    array[x] = array[x].split('|,')
    for y in array[x]:
        #print (y)
        y = y.strip('|')
        #print (y)
print(array)

