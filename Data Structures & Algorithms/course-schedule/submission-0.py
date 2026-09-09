class GraphNode:
    def __init__(self, course):
        self.course = course
        self.reqFor = set()
        self.preqs = set()

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = []
        # initialize all nodes
        for i in range(numCourses):
            node = GraphNode(i)
            nodes.append(node)
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            preq = prerequisites[i][1]
            nodes[course].preqs.add(nodes[preq])
            nodes[preq].reqFor.add(nodes[course])
        
        completed = 0
        stack = []
        for node in nodes:
            if not node.preqs:
                stack.append(node)
        # loop find all courses with no preqs and complete them
        while stack:
            completed_course = stack.pop()
            completed += 1

            for course in completed_course.reqFor:
                course.preqs.remove(completed_course)
                if not course.preqs:
                    stack.append(course)
        
        if completed == numCourses:
            return True
        else: return False

        



        