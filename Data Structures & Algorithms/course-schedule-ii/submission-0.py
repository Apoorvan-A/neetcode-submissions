class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        adjList=defaultdict(list)

        for course,pre in prerequisites:
            adjList[pre].append(course)
            indegree[course]+=1
        
        queue=deque()

        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        res=[]
        while queue:
            curr_course=queue.popleft()
            res.append(curr_course)
            for pre in adjList[curr_course]:
                indegree[pre]-=1
                if indegree[pre]==0:
                    queue.append(pre)
        return res if len(res)==numCourses else []
    