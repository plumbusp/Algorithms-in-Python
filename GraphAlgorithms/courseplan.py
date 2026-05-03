import collections
class CoursePlan:
    def __init__(self):
        self.nodes = []
        self.courses = {}

    def add_course(self, course): # add node
        self.nodes.append(course)
        self.courses[course] = []

    def add_requisite(self, course1, course2): # add edge
        if course1 not in self.nodes:
            self.nodes.append(course1)
        if course2 not in self.nodes:
            self.nodes.append(course2)
        
        self.courses[course1].append(course2)

    def find_order(self): # topological sort
        self.state = {}
        for node in self.nodes:
            self.state[node] = 0

        self.order = []
        self.cycle = False

        for node in self.nodes:
            if self.state[node] == 0:
                self.visit(node)

        if self.cycle:
            return None
        else:
            self.order.reverse()
            return self.order


    def visit(self, node):
        if self.state[node] == 1:
            self.cycle = True
            return
        if self.state[node] == 2:
            return 
        
        self.state[node] = 1
        for next_node in self.courses[node]:
            self.visit(next_node)

        self.state[node] = 2
        self.order.append(node)


if __name__ == "__main__":
    courses = CoursePlan()

    courses.add_course("Ohpe")
    courses.add_course("Ohja")
    courses.add_course("Tira")
    courses.add_course("Jym")

    courses.add_requisite("Ohpe", "Ohja")
    courses.add_requisite("Ohja", "Tira")
    courses.add_requisite("Jym", "Tira")

    print(courses.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]

    courses.add_requisite("Tira", "Tira")

    print(courses.find_order()) # None