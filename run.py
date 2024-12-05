from Client import Client


if __name__ == "__main__":
    from App import App
    app = App(client=Client(23, 45))
    app.main()