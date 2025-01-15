class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack=[]
        s=set()
        s.add(0)
        stack=rooms[0]
        n=len(rooms)
        while stack:
            k=stack.pop()
            if k not in s:
                s.add(k)
                if len(rooms[k])==0:
                    s.add(k)
                for i in rooms[k]:
                    if i not in s:
                        stack.append(i)
        if len(s)==n:
            return True
        else:
            return False
#注意空列表时的讨论
#还可以优化：（用内置的extend)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # Stack method dfs
        visited = set()
        stack = []

        # Visit room 0
        visited.add(0)
        stack.extend(rooms[0])

        # Visit all rooms with key
        while stack:
            i = stack.pop()
            if i not in visited:
                visited.add(i)
                stack.extend(rooms[i])

        return len(visited) == len(rooms)