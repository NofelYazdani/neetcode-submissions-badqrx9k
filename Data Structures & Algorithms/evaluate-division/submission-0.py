class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) # [neighour, weight]
        result = []
        for i, j in enumerate(equations):
            a, b = j
            adj[a].append([b, values[i]]) #a->b->c
            adj[b].append([a, 1/values[i]]) # c->b->a

            def bfs(src, tar):
                #base case (x)
                if src not in adj or tar not in adj:
                    return -1
                
                queue = deque([(src, 1)])
                visited_element = set()
                visited_element.add(src)

                while queue:
                    element, weight = queue.popleft()
                    if element == tar:
                        return weight 
                    for neighbor, new_weight in adj[element]:
                        if neighbor not in visited_element:
                            visited_element.add(neighbor)
                            queue.append((neighbor, weight * new_weight))
                return -1

        for i in queries:
            #pass in source and target for each query
            result.append(bfs(i[0], i[1]))
        return result


        