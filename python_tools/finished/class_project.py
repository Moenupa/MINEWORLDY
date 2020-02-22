#python version 3.7.4
#coding *-utf-8-



def init_states():
    '''
    This function generates all states, represented by 9 characters of Ws or Es
    Input: None
    Output: list of all states consisting of 9 EWs
    '''
    s = 'EW'
    all_states = list(
        a+b+c+d+e+f+g+h+i for a in s for b in s for c in s for d in s for e in s for f in s for g in s for h in s for i in s
    )
    return all_states
    
def init_description():
    '''
    This function initializes the description for the final printout
    Input: None
    Output: None
    Description stored in global variables
    '''
    global pst, plural, identity, valid_nodes, flag
    
    pst = {'E': ('east', 'west'), 'W': ('west', 'east')}    #describes movement
    plural = {1: 'goes', 2: 'go'}                           #describes the verb
    identity = {                                            #identity describes the subject
        0:'Boat',1:'Moses',2:'Pharaoh',3:'Ahab',4:'Jezebel',5:'servant of Ahab',6:'Ananias',7:'Sapphira',8:'servant of Ananias'
    }
    valid_nodes = []                                        #initializes the valid_nodes list
    flag = False                                            #describes printout status (to print or not to print)
    
def init_graph(list_legal):
    '''
    This function generates graph which links neighbor nodes
    Input: list_legal as a whole list of legal states
    Output: dictionary of connecting legal states
    '''
    dict_link = {}
    for i in list_legal:
        list_j = list(j for j in list_legal if judge_move(i,j))
        if list_j:
            dict_link[i] = list_j
    return dict_link
    
def judge_state(state):
    '''
    This function judges whether a state is legal
    Input: position state (9 EWs)
    Output: True if legal / False if illegal
    '''
    flag = True
    #elif structure simplifies judging times
    if state[1] != state[2] and state[2] in state[3:]:
        flag = False
    elif state[3] != state[6] and state[6] in state[4:6]:
        flag = False
    elif state[3] != state[6] and state[3] in state[7:]:
        flag = False
    elif state[0] not in (state[1:4]+state[6:7]):
        flag = False
    
    return flag
    
def judge_move(s1, s2):
    '''
    This function judges whether the movsement between two states is legal
    Input: two states s1, s2
    Output: True if legal / False if illegal
    '''
    chg,corrected = differ(s1 = s1, s2 = s2, correct = True)
    flag = (len(chg) == 2 or len(chg) == 3) and (0 in chg) and (1 in chg or 2 in chg or 3 in chg or 6 in chg) and corrected
    return flag
    
def differ(s1, s2, correct = False):
    '''
    This function finds the index of differences between state s1 and s2
    Input: s1 and s2 as two states with same length of 9, correct to constraint person movement parallel to boat movement
    Output: index as a list including index of different element
    If mode indicator 'correct' is True, the difference is exclusive
    '''
    index = list(i for i in range(9) if s1[i] != s2[i])
    
    if correct:
        correction = list(i for i in range(9) if s1[i] != s2[i] and s1[i] == s1[0])
        flag = (index == correction)
        return index, flag
    
    else:
        return index
        
def get_shortest_path(graph, start = 'EEEEEEEEE', end = 'WWWWWWWWW', path=[]):
    '''
    This function finds a shortest path from 'start' to 'end' on a graph
    Input: graph, start, end
    Output: formatted changes along the shortest path (human readable)
    '''
    list_path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    
    shortest_path = None
    
    for node in graph[start]:
        if node not in path:
            new_path = get_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    
    if shortest_path:
        return formatted_printout(shortest_path+['WWWWWWWWW'])
        
def formatted_printout(path):
    '''
    This function formats the path nodes to human-readable movements
    Input: a list of nodes on the shortest path
    Output: move statement
    '''
    global valid_nodes, flag, pst, plural, identity
    if path:
        if flag:
            try:
                for i in range(1,len(path)):
                    index = differ(s1 = path[i-1], s2 = path[i])[1:]
                    #index stores the index of difference between two states
                    
                    print(
                        'East: {ppl_e}\nWest: {ppl_w}\n({No}) \t {subject} {verb} from the {dep} to the {des}.\n'.format(
                            ppl_e = sorted([identity[x] for x in range(9) if path[i-1][x] == 'E']),
                            ppl_w = sorted([identity[x] for x in range(9) if path[i-1][x] == 'W']),
                            No = i, subject = ' and '.join(identity[z] for z in index),
                            verb = plural[len(index)], dep = pst[path[i][0]][0], des = pst[path[i][0]][1]
                        )
                    )
            except KeyError:
                flag = False
        else:
            for node in path:
                valid_nodes.append(node)
            valid_nodes = sorted(list(set(valid_nodes)))
    
def procs(heading, content = [], mode = 'legalstate'):
    '''
    This function processes the print output in a specific format
    Input: heading as the heading, content as the content under the heading
    Output: formatted printing of output
    '''
    length = len(content)
    
    if mode == 'legalstate':
        print('{heading}: ({length})'.format(heading = heading, length = length))
    
    elif mode == 'title':
        print(heading.upper())
    
    elif mode == 'graph':
        print('There are {length} legal states that are {heading} shortest path.'.format(length = length, heading = heading))
    
    elif mode == 'illegalstate':
        print('The set of illegal states that violate {heading}: ({length})'.format(heading = heading, length = length))
    
    #above code process the description for states, code below print specific states
        
    if content:
        if type(content) == type(list()):
            for i in range(length):
                print(
                    '\n'+content[i] if (i % 6 == 0) else content[i], end = ' '
                )
            print('')
        
        elif type(content) == type(dict()):
            print('')
            for key, value in graph.items():
                print('{key} {value}'.format(key = key, value = value))
    print('')
    
def main():
    '''
    main solver program to the river-crossing problem
    Input: None
    Output: Human-readable statement of solution to the river-crossing problem
    '''
    global legal_states, graph, valid_nodes, flag

    init_description()
    all_states = init_states()
    legal_states = [i for i in all_states if judge_state(i)]
    illegal_states = [i for i in all_states if i not in legal_states]
    
    graph = init_graph(legal_states)
    get_shortest_path(graph)
    graph = init_graph(valid_nodes)
    
    #SECTION A STATE PRINTOUT
    procs(heading = 'section a: the state space', mode = 'title')
    procs(heading = 'The set of legal states', content = legal_states)
    
    list_C1 = [i for i in illegal_states if i[0] not in [i[1],i[2],i[3],i[6]]]  #illegal states C1
    list_C2 = [i for i in illegal_states if i[1] != i[2] and i[2] in i[3:]]     #illegal states C2
    list_C3 = [i for i in illegal_states if i[3] != i[6] and i[6] in i[4:6]]    #illegal states C3
    list_C4 = [i for i in illegal_states if i[3] != i[6] and i[3] in i[7:]]     #illegal states C4
    
    dict_legal = {
        '(C1): The set of illegal states that violate the constraint of having the boat with at least a man': list_C1,
        "(C2): The set of illegal states that violate the constraint of preventing Pharaoh from beating others": list_C2,
        "(C3): The set of illegal states that violate the constraint of preventing Ananias from beating Ahab's household": list_C3,
        "(C4): The set of illegal states that violate the constraint of preventing Ahab from beating Ananias's household": list_C4
    }
    dict_illegal = {
        'both C2 and C3': list(set(list_C2).intersection(set(list_C3))),
        'both C2 and C4': list(set(list_C2).intersection(set(list_C4))),
        'both C3 and C4': list(set(list_C3).intersection(set(list_C4))),
        'C2, C3 and C4': list(set(list_C2).intersection(set(list_C3)).intersection(set(list_C4))),
        'only C2': list(set(list_C2).difference(set(list_C3)).difference(set(list_C4))),
        'only C3': list(set(list_C3).difference(set(list_C2)).difference(set(list_C4))),
        'only C4': list(set(list_C4).difference(set(list_C2)).difference(set(list_C3)))
    }
    #key-value pairs to pair up description with each list of states under the description
    
    for key,value in dict_legal.items():
        procs(heading = key, content = value)
    for key,value in dict_illegal.items():
        procs(heading = key, content = value, mode = 'illegalstate')
    
    #SECTION B GRAPH
    procs(heading = 'section b: forming a graph', mode = 'title')
    procs(heading = 'part of at least one', content = graph, mode = 'graph')
    procs(heading = 'NOT part of any', content = list(i for i in legal_states if i not in valid_nodes), mode = 'graph')
    
    #SECTION C SHORTEST PATH
    procs(heading = 'section c: shortest paths', mode = 'title')
    flag = True
    get_shortest_path(graph)
    
def draw():
    '''
    This function draws the graph
    Input: graph as the dictionary of linking nodes
    Output: visualized graph
    '''
    global valid_nodes, graph
    neighborNodes = [
        (i,j) for i in valid_nodes for j in valid_nodes if j in graph[i]
    ]
    
    import networkx
    import matplotlib.pyplot as plt
    G = networkx.Graph()
    G.add_nodes_from(valid_nodes)
    G.add_edges_from(neighborNodes)

    networkx.draw(G,with_labels = True, edge_color = 'r', node_color = 'g',node_size=1000)
    plt.show()

main()