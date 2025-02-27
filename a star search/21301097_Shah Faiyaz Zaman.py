import heapq,math
file_inp=open("input_file.txt",'r')
initial_read=file_inp.read().split('\n') #reads entire file as one and splits every new line 
heuristics={}
visited={} #will track heuristicc+actual path cost, actual path cost from source node to dest and all nodes req
graph=[[]]
graph_index_pos={} #since the cities arent arranged alphabetically a dicct is kept to keep index for list of list graph method, probably dict based graph would've been better
path_trace={} #will keep a track of parent of every node. In case (from graph) if a node can be approached through multiple parents only the shortest and relevant node will be stored
counter=1  #to keep pos 0 of list of list empty
for i in initial_read:
    test=i.split(' ')
    heuristics[test[0]]=int(test[1])
    visited[test[0]]=[math.inf,math.inf] #visited[city name]=[heuristic+actualpath cost, actual path cost] actual path cost is also saved to output final distance, init as inf
    graph_index_pos[test[0]]=counter  #marks index in graph
    path_trace[test[0]]=None  #initially parent for each node is kept empty
    counter+=1
    
    directions=[]
    for j in range(2,len(test)-1,2):
        directions.append([test[j],int(test[j+1])])
        
    graph.append(directions)  #merge graph
def A_star_test(graph,heuristics,start_city,end_city):
    heap_queue=[]  #priority queue


    heapq.heappush(heap_queue,(0+heuristics[start_city],start_city,0)) # 0+ heuristic, city name and acctual distance pushed 
    visited[start_city]=[heuristics[start_city],0] #start city is marked in visited
   
    while len(heap_queue)!=0:

        current=heapq.heappop(heap_queue) #pop value based on smallest heuristic+actual path cost
     
        current_city=current[1]
        current_dist=current[2]
        adjacent_cites=graph[graph_index_pos[current_city]] #retrieve the cities from which we can go from current city
       
        for i in range (len(adjacent_cites)):
            if adjacent_cites[i][0]==end_city:  #if goal city reached
                if visited[adjacent_cites[i][0]][0]>adjacent_cites[i][1]+current_dist+heuristics[adjacent_cites[i][0]]:   #checks if a there exists a better path already using sum of heuristics and path cost
                    visited[adjacent_cites[i][0]]=[adjacent_cites[i][1]+current_dist+heuristics[adjacent_cites[i][0]],adjacent_cites[i][1]+current_dist] 
                    path_trace[adjacent_cites[i][0]]=current_city
            
            else: 
                
                
                if visited[adjacent_cites[i][0]][0]>adjacent_cites[i][1]+current_dist+heuristics[adjacent_cites[i][0]]: #checks if a there exists a better path already
                    visited[adjacent_cites[i][0]]=[adjacent_cites[i][1]+current_dist+heuristics[adjacent_cites[i][0]],adjacent_cites[i][1]+current_dist] #if so visited stores the combined val and actual path cost
                    path_trace[adjacent_cites[i][0]]=current_city #parent for that ccity is marked, based on shortest path
                    heapq.heappush(heap_queue,(adjacent_cites[i][1]+current_dist+heuristics[adjacent_cites[i][0]],adjacent_cites[i][0],adjacent_cites[i][1]+current_dist)) #pushed in to priority queue

    #print(path_trace)
    path=[]
    test=end_city
    path.append(test)
    while test!=start_city:
        test=path_trace[test]  #using path _trace actual cities needed to cover is entered into the list, if there's none in between then no path exists as its broken
        if test==None:
            return 'No path'
        path.append(test)
    true_ans=[]
    for i in range(len(path)-1,-1,-1): #as we start entering city names from goal to soource, this path reverses it
        true_ans.append(path[i])
    for i in range(len(true_ans)-1):
        print(true_ans[i],end='-->')
    print(true_ans[len(true_ans)-1],end='')  #print  for path

    print()
   
    print('Total distance:',visited[end_city][1],'km') #print for distance


 

A_star_test(graph,heuristics,input('Start node: '),input('End node: '))