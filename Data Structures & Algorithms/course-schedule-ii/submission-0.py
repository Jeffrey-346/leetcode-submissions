class GraphNode:
    def __init__(self, course):
        self.course = course
        self.reqFor = set()
        self.preqs = set()

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

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
        
        stack = []
        for node in nodes:
            if not node.preqs:
                stack.append(node)
        # loop find all courses with no preqs and complete them
        schedule = []
        while stack:
            completed_course = stack.pop()
            schedule.append(completed_course.course)

            for course in completed_course.reqFor:
                course.preqs.remove(completed_course)
                if not course.preqs:
                    stack.append(course)
        
        if len(schedule) != numCourses:
            return []
        else: return schedule
        