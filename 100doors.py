'''
100 doors skript
'''

open = 'open'
closed = 'closed'
doors_list = [closed] * 100
number_of_doors = 100

for i in range(number_of_doors):
    for j in range(i, number_of_doors, i+1):
        if doors_list[j] == open:
            doors_list[j] = closed
        elif doors_list[j] == closed:
            doors_list[j] = open

opened_door = []
for i in range(number_of_doors):
    if doors_list[i] == open:
        opened_door.append(str(i+1))

print('The following doors are open:', ', '.join(opened_door))