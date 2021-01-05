def update_data():
    data = 'data/current_data.csv'
    log = 'puttyLOG/putty_log.txt'
    output = open(data, 'w')
    start = False
    i = 1
    num = 0
    with open(log, 'r') as text:
        for line in text:
            num += line.count('POS')

    with open(log, 'r') as text:
        for line in text:
            if 'POS' in line:
                if i == num:
                    start = True
                    line = 'POS;FW;RW;TO;TC\n'
                i += 1
            if 'max' in line:
                start = False
            if start:
                line = line.replace('\t', ';')
                output.write(line)
    text.close()

    return data
