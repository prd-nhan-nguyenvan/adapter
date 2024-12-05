from ColorClient import ColorClient


if __name__ == "__main__":
    from App import App
    app = App(client=ColorClient(23, 45))
    app.main()