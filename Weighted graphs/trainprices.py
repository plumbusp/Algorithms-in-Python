class TrainPrices:
    def __init__(self):
        self.graph = {} #adjacency matrix
        self.cities = []

    def add_city(self, name):
        self.cities.append(name)

    def add_train(self, city1, city2, price):
        self.graph[(city1,city2)] = price
        self.graph[(city2,city1)] = price

    def find_prices(self): #Floyd Warshall
        distances = {}
        # first create the current graph with shortest distance form one to another
        for a in self.cities:
            for b in self.cities:
                if a == b:
                    distances[(a,b)] = 0
                elif (a,b) in self.graph:
                    distances[(a,b)] = self.graph[(a,b)]
                else:
                    distances[(a,b)] = float("inf")

        # loop and find wether there is middle man
        for k in self.cities:
            for a in self.cities:
                for b in self.cities:
                    # check if the old distance longer than with middleman
                    new_price = min(distances[(a,b)], # price of train from a to b
                                    distances[(a,k)]
                                    + distances[(k,b)])
                    distances[(a,b)] = new_price
                    
        # formating the result
        formatted = []
        sorted_cities =  sorted(self.cities)
        formatted.append([None] +sorted_cities)
        for city1 in sorted_cities:
            entry = [city1]
            for city2 in sorted_cities:
                price = distances[(city1, city2)]
                if price == float("inf"):
                    price = -1
                entry.append(price)
            formatted.append(entry)
                
        return formatted
                    

if __name__ == "__main__":
    prices = TrainPrices()

    prices.add_city("Helsinki")
    prices.add_city("Turku")
    prices.add_city("Tampere")
    prices.add_city("Oulu")

    prices.add_train("Helsinki", "Tampere", 20)
    prices.add_train("Helsinki", "Turku", 10)
    prices.add_train("Tampere", "Turku", 50)

    listt = prices.find_prices()
    for entry in listt:
        print(entry)

    # metodin haluttu tulos:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]