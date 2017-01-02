import heapq

def search_astar(start, h_func, poss_func):
    q = [(h_func(start), start)]
    visited = {start: None}
    cost = {start: 0}
    while q:
        h, state = heapq.heappop (q)
        if h_func(state) == 0:
            path = []
            while state != start:
                path.append (state)
                state = visited[state]
            return path
        poss = poss_func (state)
        for p in poss:
            new_cost = cost[state]+1
            if p not in cost or new_cost < cost[p]:
                heapq.heappush(q, (new_cost + h_func(p), p))
                cost[p] = new_cost
                visited[p] = state
    return 0