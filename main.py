print("AoC2021 day3 part1)

current_measurement = 0  #current
previous_measurement = 0  #previous
increase_count = 0 #increase counter
count = 0

file1 = open('inputAoC2021day1.txt', 'r')
Lines = file1.readlines()

for line in Lines:

    current_measurement = int(line)

    if current_measurement>previous_measurement and count != 0:
        increase_count += 1
#        print("increasing")
#    elif current_measurement<previous_measurement and count != 0:
#        print("decreasing")

    previous_measurement = current_measurement
    count += 1

print("done.......")
print("number of increase=",increase_count)


print("AoC2021 day3 part 2")

A0 = 0
A1 = 0
A2 = 0

current_average_measurement = 0  #current
previous_average_measurement = 0  #previous
increase_average_count = 0 #increase counter
count = 0
line_count = 0
averages = 3

file1 = open('inputAoC2021day1.txt', 'r')
Lines = file1.readlines()

#count number of lines in file
for line in Lines:
    if line != "\n":
        line_count += 1

print("number of lines in file = ",line_count)

for line in Lines:
    if(count<1998):
        A0 = int(Lines[count])
        A1 = int(Lines[count+1])
        A2 = int(Lines[count+2])
        current_average_measurement = A0 + A1 + A2
#    print("current average",current_average_measurement)
#    print("previous average",previous_average_measurement)


#    current_average_measurement = int(line) + (line+1 + int(line+2)

    if (current_average_measurement>previous_average_measurement and count!=0):
        increase_average_count += 1

    previous_average_measurement = current_average_measurement

    count += 1
print("done.......")
print("number of increase=",increase_average_count)