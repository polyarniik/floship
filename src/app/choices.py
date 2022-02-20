from djchoices import DjangoChoices, ChoiceItem


class StatusChoices(DjangoChoices):
    NEW = ChoiceItem("NEW", "New")
    ACCEPTED = ChoiceItem("ACCEPTED", "Accepted")
    SEND = ChoiceItem("SEND", "Send")
    IN_DELIVERY = ChoiceItem("IN_DELIVERY", "In delivery")
    STORED = ChoiceItem("ACCEPTED", "Stored")
