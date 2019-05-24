def process_movement(movements, facing, position, field):
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
            if position[1] < field[1]:
                position=(position[0], position[1]+1)        
        if commands == "M" and facing=="S":
            if position[1] > 0:
                position=(position[0], position[1]-1) 
        if commands == "M" and facing=="E":
            if position[0] < field[0]:
                position = (position[0] + 1, position[1]) 
        if commands == "M" and facing=="W":
            if position[0] > 0:
               position=(position[0] - 1, position[1])
    return print("Final position: " + str(position[0]) + " " + str(position[1]) + " " + facing)           

def rover(entry_string):
    new_string = entry_string.split(" ")

    if int(new_string[0])>=0 and int(new_string[1])>=0:      
        field = (int(new_string[0]),int(new_string[1])) 

    position=(new_string[2], new_string[3])
    
    facing = new_string[4]
    print("Initial position : " + str(position[0]) + " " + str(position[1]) + " " + facing)
    process_movement(new_string[5], facing, position, field)

rover("5 5 1 2 N MM")
rover("5 5 1 2 N MMRMMRMM")
rover("5 5 1 2 N MMMMMMM")
rover("5 5 1 2 N LLLMM")