from Client import Client
from ColorOutput import ColorOutput

class ColorClient(Client):
    def _output(self):
        colored_sum = ColorOutput.color('OKGREEN', "The sum of the two numbers is: " + str(self.sum))
        print(colored_sum)