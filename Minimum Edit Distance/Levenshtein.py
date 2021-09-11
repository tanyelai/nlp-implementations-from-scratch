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


def LevenshteinDistance(dist, source, target):
    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):
            if source[i-1] == target[j-1]:
                dist[i][j] = dist[i-1][j-1]
            else:
                dist[i][j] = 1 + min( dist[i-1][j],
                              dist[i][j-1],
                              dist[i-1][j-1])

    return int(dist[len(source)][len(target)])


###### MAIN ######
source = "lakers"
target = "ahm"
s_len = len(source)
t_len = len(target)

dist = np.matrix
dist = Initialization(s_len, t_len)

print("Result: ", LevenshteinDistance(dist, source, target))
print("\nEdit distance grid:")
Print(dist, s_len, t_len)