from notification.notifier import Notifier


class SlackNotifier(Notifier):
    TYPE = "slack"

    def __init__(self):
        raise NotImplementedError("SlackNotifier is not implemented yet.")

    def send(self, to_email, subject, message):
        raise NotImplementedError("SlackNotifier is not implemented yet.")
