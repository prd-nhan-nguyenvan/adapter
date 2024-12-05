from Client import Client

class App:
    def __init__(self, client: Client):
        self.client = client

    def run(self):
        self.client.process()

    def main(self):
        self.run()