class Contest:
    def __init__(self, names, task_count):
        self.counter = 0
        self.taskCount = task_count
        self.bestScores = {name: [0] *(task_count + 1) for name in names}
        self.timeStamps = {name: 0 for name in names}
        self.totals = {name: 0 for name in names}

    def add_submission(self, name, task, score):
        self.counter += 1
        oldTotal = 0
        for i in range(1, self.taskCount+1):
            oldTotal = oldTotal + self.bestScores[name][i]
        if score > self.bestScores[name][task]:
            self.bestScores[name][task] = score
        newTotal = 0
        for i in range(1, self.taskCount + 1):
            newTotal = newTotal + self.bestScores[name][i]
        if newTotal > oldTotal:
            self.timeStamps[name] = self.counter
        self.totals[name] = newTotal

    def create_scoreboard(self):
        names = list(self.totals.keys())
        names.sort()

        def Key(name):
            total = self.totals[name]
            if total== 0:
                return (0, 0, name)
            return (total *-1, self.timeStamps[name], name)
        
        names = sorted(names, key=Key)
        return [(name, self.totals[name]) for name in names]

if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]