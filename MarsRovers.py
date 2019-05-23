string_entrada = "5 5 1 2 N LMLMLMLMM 3 3 E MMRMMRMRRM"
new_string = string_entrada.split(" ")
print(new_string)

if int(new_string[0])>=0:
    map_x= new_string[0]
if int(new_string[1])>=0:
    map_y = new_string[1]

initial_pos_x = new_string[2]
initial_pos_y = new_string[3]




print(map_x + " " + map_y)
print(initial_pos_x + " " + initial_pos_y)