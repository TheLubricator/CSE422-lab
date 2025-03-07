import math
import random
class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.value=None
def strength(x):
    return math.log(x+1,2)+(x/10)
def utility(maxV,minV):
    return strength(maxV)-strength(minV)+(-1)**(random.randint(0,1))*(random.randint(1,10)/10)


def TreeMaker(maxV,minV): 
    stack=[]
    root=Node()
    stack.append(root)
    for i in range(5):
        test=[]
        while len(stack)!=0:
            cur=stack.pop()
            cur.left=Node()
            if i==4:
                cur.left.value=round(utility(maxV,minV),2)
            
            cur.right=Node()
            if i==4:
                cur.right.value=round(utility(maxV,minV),2)
          
            test.append(cur.left)
            test.append(cur.right)
            
        stack=stack+test
    return root

def max_value(state,alpha,beta):
    v=-math.inf 
    if state.left==None and state.right==None:
        return state.value
    v=max(v,min_value(state.left,alpha,beta))
    v=max(v,min_value(state.right,alpha,beta))
    if v>=beta:
        return v
    alpha=max(alpha,v)
    return v    
def min_value(state,alpha,beta):
    v=math.inf  
    if state.left==None and state.right==None:
        return state.value
    v=min(v,max_value(state.left,alpha,beta))
    v=min(v,max_value(state.right,alpha,beta))
    if v<=alpha:
        return v
    beta=min(beta,v)        
    return v
def NumberAlternator(prev_num):
    if prev_num==0:
        return 1
    elif prev_num==1:
        return 0
def Chess_Masters(first_player_select,Carlsen_str,Caruana_str):
    match_results={'Caruana':0, 'Carlsen':0,'Draw':0}
    for i in range(4):
        if first_player_select==0:
            the_tree=TreeMaker(Carlsen_str,Caruana_str)
            result=max_value(the_tree,-math.inf,math.inf)
            if result>0:
                print('Game',str(i+1),'Winner: Magnus Carlsen (Max)'+'('+'Utility value: '+str(result)+')')
                match_results['Carlsen']+=1
            elif result<0:
                print('Game',str(i+1),'Winner: Fabiano Caruana (Min)'+'('+'Utility value: '+str(result)+')')
                match_results['Caruana']+=1
            elif result==0:
                print('Game',str(i+1),'Winner: Match drawn')
                match_results['Draw']+=1
            first_player_select=NumberAlternator(first_player_select) 
        elif first_player_select==1:
            the_tree=TreeMaker(Caruana_str,Carlsen_str)
            result=max_value(the_tree,-math.inf,math.inf)
            if result>0:
                print('Game',str(i+1),'Winner: Fabiano Caruana (Max)'+'('+'Utility value: '+str(result)+')')
                match_results['Caruana']+=1
            elif result<0:
                print('Game',str(i+1),'Winner: Magnus Carlsen (Min)'+'('+'Utility value: '+str(result)+')')
                match_results['Carlsen']+=1
            elif result==0:
                print('Game',str(i+1),'Winner: Match drawn')
                match_results['Draw']+=1
            first_player_select=NumberAlternator(first_player_select)
    return match_results

player_select=int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
Carlsen_Str=round(float(input("Enter base strength for Carlsen: ")),2)
Caruana_Str=round(float(input("Enter base strength for Caruana: ")),2)
result=Chess_Masters(player_select,Carlsen_Str,Caruana_Str)

print()
print("Overall Results:")
print('Magnus Carlsen Wins:',str(result['Carlsen']))
print('Fabiano Caruana Wins:',str(result['Caruana']))
print('Draws:',str(result['Draw']))
print("Overall Winner: ", end='')

if result['Carlsen']==result['Caruana']:
    print('Draw')
elif result['Carlsen']>result['Caruana']:
    print("Magnus Carlsen")
elif result['Carlsen']<result['Caruana']:
    print("Fabiano Caruana")

def max_value_MindControl(state,alpha,beta):
    v=-math.inf
   
    if state.left==None and state.right==None:
        return state.value
   
    v=max(v,max_value_MindControl(state.left,alpha,beta))
    v=max(v,max_value_MindControl(state.right,alpha,beta))
    if v>=beta:
        return v
    alpha=max(alpha,v)
    return v    
print()
print("#################################################################")
print()
def Rigged_ChessMatch(player_select,mindcontrol_str,Light_str,L_str):
    if player_select==0:
        the_tree=TreeMaker(Light_str,L_str)
        true_result=max_value(the_tree,-math.inf,math.inf)
        rigged_Result=max_value_MindControl(the_tree,-math.inf,0)
        rigged_result_minus_cost=round(rigged_Result-mindcontrol_str,2)
        print("Minimax value without Mind Control: ",str(true_result))
        print("Minimax value with Mind Control: ", str(rigged_Result))
        print("Minimax value with Mind Control after incurring the cost: ",str(rigged_result_minus_cost))
        print()

        if true_result>0:
            if rigged_result_minus_cost>0:
                print("Light should NOT use Mind Control as the position is already winning.")
            else:
                print("Light should NOT use Mind Control as it backfires.")    
        else:
            if rigged_result_minus_cost<0:
                print("Light should NOT use Mind Control as the position is losing either way.")
            else:
                print("Light should use Mind Control.")
    elif player_select==1:
        the_tree=TreeMaker(L_str,Light_str)
        true_result=max_value(the_tree,-math.inf,math.inf)
        rigged_Result=max_value_MindControl(the_tree,-math.inf,0)
        rigged_result_minus_cost=rigged_Result-mindcontrol_str
        print("Minimax value without Mind Control: ",str(true_result))
        print("Minimax value with Mind Control: ", str(rigged_Result))
        print("Minimax value with Mind Control after incurring the cost: ",str(rigged_result_minus_cost))
        print()

        if true_result>0:
            if rigged_result_minus_cost>0:
                print("L should NOT use Mind Control as the position is already winning.")
            else:
                print("L should NOT use Mind Control as it backfires.")    
        else:
            if rigged_result_minus_cost<0:
                print("L should NOT use Mind Control as the position is losing either way.")
            else:
                print("L should use Mind Control.")

player_select=int(input("Enter who goes first (0 for Light, 1 for L): "))
mindcontrol_str=round(float(input("Enter the cost of using Mind Control:")),2)
Light_Str=round(float(input("Enter base strength for Light: ")),2)
L_Str=round(float(input("Enter base strength for L: ")),2)
Rigged_ChessMatch(player_select,mindcontrol_str,Light_Str,L_Str)