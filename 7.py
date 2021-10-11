file = open("7_input.txt", "r")
lines = file.read().splitlines()

wires = {'b':16076} # hotwire for part 2

def readinstruction(string):

    instruction = string.split(' ')

    if instruction[-1] == 'b': # hotwire for part 2

        return ['skipped'] 
    
    index = 0
    for i in instruction[:-1]:

        if i.isalpha() and i not in ['AND','OR','NOT','LSHIFT','RSHIFT','->']:
            try:
                instruction[index] = int(wires[i])
            except KeyError:
                instruction[index] = 'skipped'

        elif i.isdigit():
                instruction[index] = int(i)

        index += 1

    return instruction

def executeinstruction(instruction):

    if 'skipped' in instruction:

        pass
    
    elif 'AND' in instruction:

        wires[instruction[4]] = instruction[0] & instruction[2]

    elif 'OR' in instruction:

        wires[instruction[4]] = instruction[0] | instruction[2]

    elif 'NOT' in instruction:

        wires[instruction[3]] = (~ instruction[1]) + 1 + 65535

    elif 'LSHIFT' in instruction:

        wires[instruction[4]] = instruction[0] << instruction[2]

    elif 'RSHIFT' in instruction:

        wires[instruction[4]] = instruction[0] >> instruction[2]

    else:    # assignment
        wires[instruction[2]] = instruction[0]

while True:
    for line in lines:
        executeinstruction(readinstruction(line))
    try:
        print(wires['a'])
        
    except:
        pass

