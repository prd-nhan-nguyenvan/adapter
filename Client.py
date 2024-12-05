class Client:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        self.sum = 0
    
    def process(self):
        self._calculate_sum()
        self._output()

    def _calculate_sum(self):
        self.sum = self.a + self.b    

    def _output(self):
        print("The sum of the two numbers is:", self.sum)

