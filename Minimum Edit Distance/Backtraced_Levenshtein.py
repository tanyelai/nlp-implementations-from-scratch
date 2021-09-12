import numpy as np
from pandas import DataFrame

def LevenshteinDistance(dist, source, target, del_cost, ins_cost, sub_cost):
    
    for j in range(1, len(target)+1):
        for i in range(1, len(source)+1):
            if source[i-1] == target[j-1]:
                dist[i][j] = dist[i-1][j-1]
            else:
                dist[i][j] = min( dist[i-1][j] + del_cost,     ## Remove
                                  dist[i][j-1] + ins_cost,     ## Insert  
                                  dist[i-1][j-1] + sub_cost )  ## Replace

    back = (Backtrace(dist, source, target))
    print("The coordinates of the path: \n",back[0])
    print("\n '^' correspond to insertion, '<-' correspond to deletion ")
    print("new source: ", back[1])
    print("new target: ", back[2])

    edit_distance = dist[len(source)][len(target)]
    return edit_distance, dist


##### BACKTRACING 
def Backtrace(dist, source, target):
    
    s_len, t_len = len(source), len(target)
    src, tar= [char for char in source], [char for char in target]
    new_src, new_tar = [], []
    bt = [[s_len, t_len]]
    

    while True:
    
        if src[s_len-1] == tar[t_len-1]:
            cost = 0 
        else:
            cost = 2
        
        del_ = dist[s_len-1][t_len]
        ins_ = dist[s_len][t_len-1]
        sub_ = dist[s_len-1][t_len-1]
        main = dist[s_len][t_len]
                    
        #### WE PREFER TO GO DIAGONALLY SO WE FIRST CHECK IS THERE ANY COST FOR
        #### GOING AS SUB ( DIAG )
        if main == sub_ + cost:
            bt.append([s_len-1, t_len-1])
            new_src = [src[s_len-1]] + new_src
            new_tar = [tar[t_len-1]] + new_tar
        
            s_len, t_len = s_len-1, t_len-1
            
        else:
            #### CHECKING FOR IT IS DELETED OR INSERTED 
            #### DEL = ( <- ): LEFT 
            #### INSERT ( ^ ): UP
            
            if main == del_ + 1:
                bt.append([s_len-1, t_len])
                new_src = [src[s_len-1]] + new_src
                new_tar = ["<-"]  + new_tar
                
                s_len = s_len-1
                
            elif main == ins_ + 1:
                bt.append([s_len, t_len-1])
                new_src = ["^"] + new_src
                new_tar = [src[t_len-1]] + new_tar
                
                t_len = t_len-1
        
        if s_len == 0 or t_len == 0:
            return bt, new_src, new_tar



######## MAIN ########
source = "insertion"
target = "execution"
s_len = len(source)
t_len = len(target)
del_cost, ins_cost, sub_cost = 1, 1, 2
dist = np.zeros((s_len+1, t_len+1))
    
for i in range(s_len+1):
    dist[i][0] = i
        
for j in range(t_len+1):
    dist[0][j] = j

res = LevenshteinDistance(dist, source, target, del_cost, ins_cost, sub_cost)
print("\nEdit distance grid:")
### another way of grid without library: 
# print('\n'.join(['\t '.join([str(cell) for cell in row]) for row in dist]))

### another way of grid with numpy library but:
# print(np.matrix(dist.astype(int))) == print(dist.astype(int))

### another way of grid with pandas library:
print(DataFrame(dist.astype(int)))


print("\nEdit distance: ", int(res[0]))
