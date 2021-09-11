import numpy as np

def Initialization(s_len, t_len):
    dist = np.zeros((s_len+1, t_len+1))
    
    for i in range(s_len+1):
        dist[i][0] = i
        
    for j in range(t_len+1):
        dist[0][j] = j
    return dist


def Print(dist, s_len, t_len):
    for i in range(s_len+1):
        for j in range(t_len+1):
            print(int(dist[i][j]), end= "   ")
        print()
    return 0 


def LevenshteinDistance(dist, source, target, del_cost, ins_cost, sub_cost):
    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):
            if source[i-1] == target[j-1]:
                dist[i][j] = dist[i-1][j-1]
            else:
                dist[i][j] = min( dist[i-1][j] + del_cost,     ## Remove
                                  dist[i][j-1] + ins_cost,     ## Insert  
                                  dist[i-1][j-1] + sub_cost)   ## Replace

    return int(dist[len(source)][len(target)])


###### MAIN ######
source = "intention"
target = "execution"

# Levenshtein also proposed an alternative version of his metric in which each insertion
# or deletion has a cost of 1 and substitutions are not allowed. 
# ( This is equivalent to allowing substitution, but giving each substitution a cost of 2
# since any substitution can be represented by one insertion and one deletion ).
del_cost, ins_cost, sub_cost = 1, 1, 2

s_len = len(source)
t_len = len(target)

dist = np.matrix
dist = Initialization(s_len, t_len)

print("Result: ", LevenshteinDistance(dist, source, target, del_cost, ins_cost, sub_cost))
print("\nEdit distance grid:")
Print(dist, s_len, t_len)