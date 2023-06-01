class Clerk:
    def __init__(self, cheap_tickets, tickets_expensive):
        self.cheap_tickets = cheap_tickets
        self.expensive_tickets = tickets_expensive

    def sell_ticket(self, ticket, customer):
        if ticket.price < customer.money:
            customer.have.append(ticket)
        if customer.wish == 'cheap':
            self.cheap_tickets -= 1
        else:
            self.tickets_expensive -= 1


class Customer:
    def __init__(self, money, wish):
        self.money = money
        self.wish = wish
        self.have = []

    def buy(self, clerk, ticket):
        if self.wish == 'cheap' and clerk.cheap_tickets:
            clerk.sell_ticket(ticket, self)
        elif self.wish == 'expensive' and clerk.tickets_expensive:
            clerk.sell_ticket(ticket, self)


class Ticket:
    def __init__(self, price, wish):
        self.price = price


Julio = Customer(8000, 'cheap')
John = Clerk(8, 12)
ticket_to_the_moon = Ticket(100, 'cheap')
Julio.buy(John, ticket_to_the_moon)

print(Julio.have)
print(John.cheap_tickets)
