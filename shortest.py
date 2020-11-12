def banch(graph, start):
 
    costs = {}                # 记录start到其他所有点的距离
    trace = {start:[start]}   # 记录start到其他所有点的路径
 
    for key in graph.keys():
        costs[key] = math.inf
    costs[start] = 0
    
    queue = [start]          # 初始化queue
    
    while len(queue) != 0:
        head = queue[0]                # 起始节点
        for key in graph[head].keys(): # 遍历起始节点的子节点
            dis = graph[head][key] + costs[head]
            if costs[key] > dis:
                costs[key] = dis
                temp = deepcopy(trace[head])  # 深拷贝
                temp.append(key)        
                trace[key] = temp# key节点的最优路径为起始节点最优路径+key
                queue.append(key)
 
        queue.pop(0)                   # 删除原来的起始节点
    print(costs)
    print(trace)