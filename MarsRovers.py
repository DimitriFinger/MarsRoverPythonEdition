def process_movement(movements, facing, pos_x, pos_y, map_size_x, map_size_y):
    for commands in movements:
        if facing == "N" and commands == "L":
            facing = "W"
        elif facing == "N" and commands == "R":
            facing = "E"    
        elif facing == "S" and commands == "L":
            facing = "E"
        elif facing == "S" and commands == "R":
            facing = "W"    
        elif facing == "W" and commands == "L":
            facing = "S"
        elif facing == "W" and commands == "R":
            facing = "N" 
        elif facing == "E" and commands == "L":
            facing = "N"
        elif facing == "E" and commands == "R":
            facing = "S"

        if commands == "M" and facing=="N":        
            if pos_y < map_size_y:
                pos_y += 1        
        if commands == "M" and facing=="S":
            if pos_y > 0:
                pos_y -= 1 
        if commands == "M" and facing=="E":
            if pos_x < map_size_x:
                pos_x += 1 
        if commands == "M" and facing=="W":
            if pos_x > 0:
                pos_x -= 1
    return print("Final position: " + str(pos_x) + " " + str(pos_y) + " " + facing)             


def rover(entry_string):
    new_string = entry_string.split(" ")


    if int(new_string[0])>=0:
        map_size_x = int(new_string[0])
    if int(new_string[1])>=0:
        map_size_y = int(new_string[1])
    
    pos_x = int(new_string[2])
    pos_y = int(new_string[3])
    facing = new_string[4]
    print("Initial position : " + str(pos_x) + " " + str(pos_y) + " " + facing)
    process_movement(new_string[5], facing, pos_x, pos_y, map_size_x, map_size_y)

#entry_string = "5 5 1 2 N MM" 
rover("5 5 1 2 N MM")
rover("5 5 1 2 N MMRMMRMM")
rover("5 5 1 2 N MMMMMMM")
rover("5 5 1 2 N LLLMM")