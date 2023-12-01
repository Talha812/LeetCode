class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        adj_list = {}
        for pair in adjacentPairs:
            if pair[0] not in adj_list:
                adj_list[pair[0]] = [pair[1]]
            else:
                adj_list[pair[0]].append(pair[1])
            if pair[1] not in adj_list:
                adj_list[pair[1]] = [pair[0]]
            else:
                adj_list[pair[1]].append(pair[0])
                
        corner = None
        for k, v in adj_list.items():
            if len(v) == 1:
                corner = k
                break
                
        curr = corner
        ans = [corner]
        prev = None

        while len(ans) < len(adj_list):
            for neigh in adj_list[curr]:
                if neigh != prev:
                    ans.append(neigh)
                    prev = curr
                    curr = neigh
                    break

        return ans