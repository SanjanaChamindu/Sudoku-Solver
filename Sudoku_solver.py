example_puzzle1=[[[5,3,0],[6,0,0],[0,9,8]],[[0,7,0],[1,9,5],[0,0,0]],[[0,0,0],[0,0,0],[0,6,0]],
[[8,0,0],[4,0,0],[7,0,0]],[[0,6,0],[8,0,3],[0,2,0]],[[0,0,3],[0,0,1],[0,0,6]],
[[0,6,0],[0,0,0],[0,0,0]],[[0,0,0],[4,1,9],[0,8,0]],[[2,8,0],[0,0,5],[0,7,9]]]

example_puzzle2=[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,1],[0,0,0],[0,0,6]],[[0,0,0],[0,0,0],[0,0,0]],
[[0,0,0],[0,0,0],[2,0,9]],[[4,0,0],[0,8,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,7]],
[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,3],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]

example_puzzle3=[[[4,6,0],[3,0,0],[0,0,9]],[[7,0,0],[0,0,0],[6,5,0]],[[1,0,2],[0,0,0],[8,7,0]],
[[0,0,1],[0,5,0],[0,8,0]],[[0,6,9],[8,2,0],[4,0,5]],[[0,5,8],[0,1,9],[0,3,6]],
[[8,1,4],[0,3,2],[0,9,0]],[[9,7,3],[0,0,6],[5,0,2]],[[0,2,0],[9,0,0],[3,4,0]]]

example_puzzle4=[[[0,8,0],[0,0,0],[0,0,0]],[[0,3,0],[0,5,0],[0,0,4]],[[4,0,0],[0,0,1],[5,8,0]],
[[0,5,7],[9,0,0],[0,3,0]],[[0,0,2],[0,0,0],[4,0,0]],[[0,9,0],[0,0,4],[6,5,0]],
[[0,7,9],[5,0,0],[0,0,6]],[[2,0,0],[0,6,0],[0,4,0]],[[0,0,0],[0,0,0],[0,2,0]]]

example_puzzle5=[[[5,3,0],[6,0,0],[0,9,8]],[[0,7,0],[1,9,5],[0,0,0]],[[0,0,0],[0,0,0],[0,6,0]],
[[8,0,0],[4,0,0],[7,0,0]],[[0,6,0],[8,0,3],[0,2,0]],[[0,0,3],[0,0,1],[0,0,6]],
[[0,6,0],[0,0,0],[0,0,0]],[[0,0,0],[4,1,9],[0,8,0]],[[2,8,0],[0,0,5],[0,7,9]]]

example_puzzle6=[[[0,0,0],[7,0,3],[4,0,0]],[[0,0,8],[1,2,9],[0,7,0]],[[0,0,0],[0,0,0],[0,9,0]],
[[3,0,0],[0,0,6],[0,0,0]],[[0,1,0],[0,0,0],[0,0,3]],[[0,0,0],[3,0,0],[0,1,7]],
[[0,0,1],[0,5,4],[0,0,0]],[[7,0,2],[3,8,0],[0,0,0]],[[0,8,9],[6,7,2],[0,0,0]]]


def is_valid(puzzle,n,x,y,z):
    for i in range (3): # Check in square
        if n in puzzle[x][i]: return False
        
    square_row=(x//3)*3
    for i in range(square_row,square_row+3): # Check in row
        if n in puzzle[i][y]: return False
        
    square_column=(x%3)
    for i in range(square_column,square_column+7,3): # Check in column
        for j in range(3):
            if n == puzzle[i][j][z]: return False
        
    return True

def possible_values_square(puzzle,x,y,z):
    possible_values=[1,2,3,4,5,6,7,8,9]

    for i in range(1,10):
        if not is_valid(puzzle,i,x,y,z):
            possible_values.remove(i)

    return possible_values

def is_solved(puzzle):
    for i in range(9):
        for j in range (3):
            if 0 in puzzle[i][j]: return False

    return True

def common_list(puzzle):
    common_items=[]
    common_coordinates=[]

    for i in range(9):
        for j in range(3):
            for k in range(3):
                if puzzle[i][j][k] ==0:
                    temp_p=possible_values_square(puzzle,i,j,k)
                    l=len(common_items)

                    if l==0:
                        common_items.append(temp_p)
                        common_coordinates.append([i,j,k])
                    else:
                        for m in range(l):
                            if len(common_items[m])>len(temp_p):
                                common_items.insert(m,temp_p)
                                common_coordinates.insert(m,[i,j,k])
                                break
                        else:
                            common_items.append(temp_p)
                            common_coordinates.append([i,j,k])
    return common_items,common_coordinates

def solve(puzzle):
    items,coordinates=common_list(puzzle)
    print(items)
    print(coordinates)
    parent_track=[]

    parent_row=0
    parent_column=0

    l=len(items)
    if l>1:
        while not is_solved(puzzle):
            print(0)
            x,y,z=coordinates[parent_row][0],coordinates[parent_row][1],coordinates[parent_row][2]
            puzzle[x][y][z]=0
            parent_solution=items[parent_row][parent_column]

            if is_valid(puzzle,parent_solution,x,y,z):
                #print(1)        
                puzzle[x][y][z]=parent_solution
                print(puzzle)       
                parent_track.append((parent_row,parent_column))
                #print(parent_track)

                if parent_row <len(items)-1:
                    child_row=parent_row+1
                else:
                    child_row=parent_row

                child_column=0
                child_solution=items[child_row][child_column]

                x_chld,y_child,z_child=coordinates[child_row][0],coordinates[child_row][1],coordinates[child_row][2]

                while not is_valid(puzzle,child_solution,x_chld,y_child,z_child):
                    print(2)
                    if child_column<len(items[child_row])-1:
                        print(4)
                        child_column+=1
                        child_solution=items[child_row][child_column]
                    
                    elif len(parent_track)>=2:
                        puzzle[x][y][z]=0
                        while True:
                            print(3)
                            if parent_column < len(items[parent_row])-1:
                                parent_column+=1
                                parent_track.pop(-1)
                                break
                            elif len(parent_track)>2:
                                x,y,z=coordinates[parent_row][0],coordinates[parent_row][1],coordinates[parent_row][2]
                                puzzle[x][y][z]=0
                                parent_track.pop(-1)
                                parent_row,parent_column=parent_track[-1][0],parent_track[-1][1]
                                print(f'{parent_row},{parent_column} 3')
                            else:
                                return 1
                        print(1000)
                        break
                    else:
                        return 2
                else:
                    parent_row=child_row
                    parent_column=child_column
                    print(100)
            else:
                puzzle[x][y][z]=0
                while True:
                    print(13)
                    if parent_column < len(items[parent_row])-1:
                        print(14)
                        parent_column+=1
                        parent_track.pop(-1)
                        print(f'{parent_row},{parent_column}*')
                        break
                    elif len(parent_track)>2:
                        x,y,z=coordinates[parent_row][0],coordinates[parent_row][1],coordinates[parent_row][2]
                        puzzle[x][y][z]=0
                        parent_track.pop(-1)
                        parent_row,parent_column=parent_track[-1][0],parent_track[-1][1]
                        x,y,z=coordinates[parent_row][0],coordinates[parent_row][1],coordinates[parent_row][2]
                        puzzle[x][y][z]=0
                        
                    else:
                        print(puzzle)
                        return 10


        else: return puzzle

def solve_(puzzle):
    items,coordinates=common_list(puzzle)
    step_track=[]
    row,column=0,0
    while not is_solved(puzzle):
        x,y,z=coordinates[row][0],coordinates[row][1],coordinates[row][2]
        step_solution=items[row][column]

        if is_valid(puzzle,step_solution,x,y,z):
            puzzle[x][y][z]=step_solution
            if not (row,column) in step_track:
                step_track.append((row,column))
            
            if row<len(items)-1:
                row+=1
                column=0
        
        elif column<len(items[row])-1:
            column+=1

        else:
            while True:
                if len(step_track)>1:
                    puzzle[x][y][z]=0

                    row,column=step_track[-1][0],step_track[-1][1]
                    x,y,z=coordinates[row][0],coordinates[row][1],coordinates[row][2]
                    puzzle[x][y][z]=0
                    step_track.pop(-1)

                    if column<len(items[row])-1:
                        column+=1
                        #step_track.pop(-1)
                        step_track.append((row,column))
                        break
                else:
                    return 0
    else:
        return puzzle



if __name__=='__main__':
    print(solve_(example_puzzle5))
                            
                    
