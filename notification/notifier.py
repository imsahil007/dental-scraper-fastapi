class Notifier:
    def __init__(self):
        pass

    def send(self, to, subject, message):
        raise NotImplementedError("Subclasses must implement this method")
