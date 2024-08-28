def parser(file):
    response = dict()
    section = '' 
    for line in file:
        newline = str(line).split(f'\\')
        for i in range(len(newline)): # 
            value = newline[i]
            if value.lower()[0:2] == 'xf':
                section = value

                if response.get(section) == None:
                    response[section] = []
            if section != '':
                response[section].append(value)
    print(response)
    return response
