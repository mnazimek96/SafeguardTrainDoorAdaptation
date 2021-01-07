file = open('test.txt', 'w')
for i in range(10):
    string = '123\n\r'
    a, b = string.split("\n")
    file.write(a)
