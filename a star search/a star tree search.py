import heapq,math
file_inp=open("input_file.txt",'r')
initial_read=file_inp.read().split('\n')
heuristics={}
visited={}
graph=[[]]
graph_index_pos={}
path_trace={}
counter=1
for i in initial_read:
    test=i.split(' ')
    heuristics[test[0]]=int(test[1])
    visited[test[0]]=math.inf
    graph_index_pos[test[0]]=counter
    path_trace[test[0]]=None
    counter+=1
    directions=[]
    for j in range(2,len(test)-1,2):
        directions.append([test[j],int(test[j+1])])
        
    graph.append(directions)
def A_star_test(graph,start_city):
    heap_queue=[]
    path=[]

    heapq.heappush(heap_queue,(0+heuristics[start_city],start_city,0)) # 0+ heuristic, city name and acctual distance pushed 
    visited[start_city]=0

    while len(heap_queue)!=0:

        current=heapq.heappop(heap_queue)
     
        current_city=current[1]
        current_dist=current[2]
        adjacent_cites=graph[graph_index_pos[current_city]]
        path.append(current_city)
        for i in range (len(adjacent_cites)):
            if adjacent_cites[i][0]=="Bucharest":
                if visited[adjacent_cites[i][0]]>adjacent_cites[i][1]+current_dist:
                    visited[adjacent_cites[i][0]]=adjacent_cites[i][1]+current_dist
                    path_trace[adjacent_cites[i][0]]=current_city
            
            else: 
                
                
                if visited[adjacent_cites[i][0]]>adjacent_cites[i][1]+current_dist:
                    visited[adjacent_cites[i][0]]=adjacent_cites[i][1]+current_dist
                    path_trace[adjacent_cites[i][0]]=current_city
                    heapq.heappush(heap_queue,(adjacent_cites[i][1]+current_dist+heuristics[adjacent_cites[i][0]],adjacent_cites[i][0],adjacent_cites[i][1]+current_dist))

    #print(path_trace)
    path=[]
    test='Bucharest'
    path.append(test)
    while test!=start_city:
        test=path_trace[test]
        if test==None:
            return 'No path'
        path.append(test)
    true_ans=[]
    for i in range(len(path)-1,-1,-1):
        true_ans.append(path[i])
    for i in range(len(true_ans)-1):
        print(true_ans[i],end='-->')
    print(true_ans[len(true_ans)-1],end='')

    print()
   
    print('Total distance:',visited['Bucharest'])

A_star_test(graph,input('Start node: '))