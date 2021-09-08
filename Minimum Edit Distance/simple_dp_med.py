def find_min_edit_distance(source, target):
    
    del_cost = 1 
    sub_cost = 2
    ins_cost = 1
    
    n = len(source)
    m = len(target)
    
    # Creating and Initialization: the zeroth row and column is the distance from the empty string
    dist = [[0 for x in range(n + 1)] for x in range(m + 1)]

    
    for i in range(m + 1):
        for j in range(n + 1):
 
            # If first string is empty, only option is to insert all characters of second string
            if i == 0:
                dist[i][j] = j    # Min. operations = j
 
            # If second string is empty, only option is to remove all characters of second string
            elif j == 0:
                dist[i][j] = i    # Min. operations = i
 
            # If last characters are same, ignore last char and recur for remaining string
            elif source[i-1] == target[j-1]:
                dist[i][j] = dist[i-1][j-1]
 
            # If last character are different, consider all possibilities and find minimum
            else:
                dist[i][j] = min(dist[i][j-1] + ins_cost,        # Insert
                                   dist[i-1][j] + del_cost,      # Remove
                                   dist[i-1][j-1] + sub_cost)    # Replace
    return dist[n][m]

print(find_min_edit_distance('insertion', 'execution'))