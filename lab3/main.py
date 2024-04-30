class TicketPriceStrategy:
    def calculate_price(self, window_seat, refundable):
        raise NotImplementedError()

class EconomyStrategy(TicketPriceStrategy):
    def calculate_price(self, window_seat, refundable):
        base_price = 100.0
        if window_seat:
            base_price += 10.0
        if not refundable:
            base_price *= 0.9  
        return base_price

class BusinessStrategy(TicketPriceStrategy):
    def calculate_price(self, window_seat, refundable):
        base_price = 200.0
        if window_seat:
            base_price += 20.0
        if not refundable:
            base_price *= 0.9  
        return base_price

class FirstClassStrategy(TicketPriceStrategy):
    def calculate_price(self, window_seat, refundable):
        base_price = 500.0
        if window_seat:
            base_price += 50.0
        return base_price

class HotTicketStrategy(TicketPriceStrategy):
    def calculate_price(self, window_seat, refundable):
        return 50.0

class Ticket:
    def __init__(self, strategy):
        self._strategy = strategy

    def calculate_price(self, window_seat, refundable):
        return self._strategy.calculate_price(window_seat, refundable)

economy_strategy = EconomyStrategy()
business_strategy = BusinessStrategy()
first_class_strategy = FirstClassStrategy()
hot_ticket_strategy = HotTicketStrategy()

economy_ticket = Ticket(economy_strategy)
business_ticket = Ticket(business_strategy)
first_class_ticket = Ticket(first_class_strategy)
hot_ticket = Ticket(hot_ticket_strategy)

# Calculate and print prices for each type of ticket
print("Economy Ticket Price:", economy_ticket.calculate_price(True, True))
print("Business Ticket Price:", business_ticket.calculate_price(False, False))
print("First Class Ticket Price:", first_class_ticket.calculate_price(True, True))
print("Hot Ticket Price:", hot_ticket.calculate_price(False, False))