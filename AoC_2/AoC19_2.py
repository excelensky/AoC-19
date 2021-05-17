import random
import copy

#read input file
input_file = open(r"C:\Users\SSelensky\Python_Files_SSE\AoC19\AoC_2\input_day2.txt","r")
#input_file = open("input_day2.txt","r")
input_data = input_file.read()
input_data_clean = list(map(int, input_data.split(",")))
#remove commas
#input_data_clean = list(map(int,input_data.replace(","," ")))
#input_data_clean
#input_data_clean = list(map(int,input_data))

def intcode_computer(intcode):
    i = 0
    while intcode[i] != 99:
        if intcode[i] == 1:
            intcode[intcode[i+3]]=intcode[intcode[i+1]]+intcode[intcode[i+2]]
        elif intcode[i] == 2:
            intcode[intcode[i+3]]=intcode[intcode[i+1]]*intcode[intcode[i+2]]
        else:
            print("FEHLER - ungültiger Wert")
            break
        i += 4
    return intcode

#Test with examples
#test_set_1 = [1,0,0,0,99]
#test_set_2 = [2,3,0,3,99]
#test_set_3 = [2,4,4,5,99,0]
#test_set_4 = [1,1,1,4,99,5,6,0,99]

# mit assert testen wie die profis
#assert intcode_computer(test_set_1) == XX, "Robin stinkt"
#assert intcode_computer(test_set_2) == ...
#assert intcode_computer(test_set_3) == ...
#assert intcode_computer(test_set_4) == ...

#solve puzzle
#input_data_clean[1] = 12
#input_data_clean[2] = 2

#gravity_assist_program = intcode_computer(input_data_clean)
#print(gravity_assist_program)
#print(gravity_assist_program[0])

#beginning part 2
#memory =
#address =
#address_0 = input_data_clean
#instruction = [opcode,input_1,input_2,output]
#instruction_pointer =
#instruction_parameters =



def brute_force_gravity_assist_2(intcode):
    memory = copy.copy(intcode)
    z = 0
    while memory[0] != 19690720:
        noun = random.randint(0,99)
        verb = random.randint(0,99)
        memory[1] = noun
        memory[2] = verb
        intcode_computer(memory)
        if memory[0] == 19690720:
            print("JUHU!!!!")
            print(f"noun:{noun}")
            print(f"verb:{verb}")
            print(f"100*noun+verb:{(100*noun+verb)}")
            break
        else:
            z += 1
            print(z)
            print(noun)
            print(verb)
            print(memory[0])
            memory = copy.copy(intcode)
    return intcode


brute_force_gravity_assist_2(input_data_clean)
