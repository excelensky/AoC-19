
import numpy as np

#read input file
Mass_data_raw = np.loadtxt(r"C:\Users\SSelensky\Python_Files_SSE\AoC19\AoC_1\Input.txt")
#Mass_Test = [14,1969,100756]

#convert to np.array to allow operations
#Mass_Test_array = np.array(Mass_Test)
Mass_array = np.array(Mass_data_raw)

#define function to calculate fuel
def fuel_calc(Mass):
    a = np.floor(Mass / 3) - 2
    return a

#calculate array with single fuels
#single_fuel = fuel_calc(Mass_array)
#print(single_fuel)

#calculate sum and print
#sum_fuel = int(np.sum(single_fuel))
#print(sum_fuel)

#define function to calculate fuel requirements for each modul
def fuel_fuel_calc(Mass):
    fuel_collect = []
    for x in Mass:
        total_fuel = fuel_calc(x)
        add_fuel = fuel_calc(x)
        while add_fuel > 0:
            add_fuel = fuel_calc(add_fuel)
            if add_fuel > 0:
                total_fuel = total_fuel + add_fuel
        fuel_collect.extend([total_fuel])
        print(total_fuel)
    return fuel_collect

Overall_fuel = fuel_fuel_calc(Mass_array)
print(Overall_fuel)

sum_fuel_fuel = int(np.sum(Overall_fuel))
print(sum_fuel_fuel)
