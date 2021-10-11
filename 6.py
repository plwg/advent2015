# read input

file = open("6_input.txt", "r")
lines = file.read().splitlines()

# store lights in a 1,000,000 list

light = [0] * 1000000


def readInstruction(string):

    
    elements = string.split(' ')

    if elements[0] == 'toggle':

        index = 0

    else:

        index = 1
    
    action = elements[index]
    x_min = elements[index + 1].split(',')[0]
    y_min = elements[index + 1].split(',')[1]
    x_max = elements[index + 3].split(',')[0]
    y_max = elements[index + 3].split(',')[1]

    return (action, x_min, x_max, y_min, y_max)

def executeInstruction(instruction):

    #print(instruction)
    
    x_min = int(instruction[1])
    x_max = int(instruction[2])
    y_min = int(instruction[3])
    y_max = int(instruction[4])
    

    for i in range(x_min, x_max + 1):

        for j in range(y_min, y_max + 1):

            if instruction[0] == "toggle":

                light[i + 1000*j] += 2

            elif instruction[0] == "on":

                light[i + 1000*j] += 1
            
            else:

                if light[i + 1000*j] - 1 < 0:

                    light[i + 1000*j] = 0

                else:

                    light[i + 1000*j] -= 1

    #print(sum(light))
    
for line in lines:
    executeInstruction(readInstruction(line))
    
print(sum(light))
