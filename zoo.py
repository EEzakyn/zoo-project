class Zoo:
    def get_ticket_price(self, age):
        if age < 0:
            return 0
        elif 0 <= age < 13: #1,2
            return 50
        elif 13 <= age < 20: #3
            return 100
        elif 20 < age <= 60: #4
            return 150
        elif age > 60:
            return 100