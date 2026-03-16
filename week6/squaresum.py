class DataAnalyzer:
    def __init__(self):
        self.material = []
        self.totalY = 0
        self.totalX = 0
        self.totalXY = 0
        self.totalXSquared = 0
        self.totalYSquared = 0

    def add_point(self, x, y):
        self.material.append((x,y))
        self.totalX += x
        self.totalY += y
        self.totalXSquared += x**2
        self.totalYSquared += y**2
        self.totalXY += y*x

    def calculate_error(self, a, b):
        return (self.totalYSquared
                - 2*a*self.totalXY
                - 2*b*self.totalY
                + a**2 * self.totalXSquared
                + 2*a*b*self.totalX
                + len(self.material)*b**2)

if __name__ == "__main__":
    analyzer = DataAnalyzer()

    analyzer.add_point(1, 1)
    analyzer.add_point(3, 2)
    analyzer.add_point(5, 3)
    print(analyzer.calculate_error(1, 0)) # 5
    print(analyzer.calculate_error(1, -1)) # 2
    print(analyzer.calculate_error(3, 2)) # 293

    analyzer.add_point(4, 2)
    print(analyzer.calculate_error(1, 0)) # 9
    print(analyzer.calculate_error(1, -1)) # 3
    print(analyzer.calculate_error(3, 2)) # 437