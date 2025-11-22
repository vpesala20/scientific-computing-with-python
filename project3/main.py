class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = sum(item['amount'] for item in self.ledger)
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        items = ""
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)
            amt = f"{entry['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{items}{total}"

def create_spend_chart(categories):
    # Calculate total spent per category
    spent = []
    for cat in categories:
        total_withdraw = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent.append(total_withdraw)
    total_spent = sum(spent)

    # Calculate percentage spent rounded down to nearest 10
    percentages = [int((s / total_spent) * 100) // 10 * 10 for s in spent]

    # Build chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for pct in percentages:
            chart += " o " if pct >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Build vertical category names
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        if i < max_len - 1:
            line += "\n"
        chart += line

    return chart