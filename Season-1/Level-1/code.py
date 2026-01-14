'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''


from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = Decimal('0')
    MAX_TOTAL = Decimal('1000000')  # maximum total amount accepted for an order
    total_expenses = Decimal('0')
    total_payments = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            # Only count valid payment amounts
            if not isinstance(item.amount, (int, float)):
                return "Invalid amount: %s" % item.amount
            amt = Decimal(str(item.amount))
            net += amt
            total_payments += abs(amt)
        elif item.type == 'product':
            # Validate quantity is a positive integer and amount is non-negative
            if not (isinstance(item.quantity, int) and item.quantity > 0):
                return "Invalid quantity: %s" % item.quantity
            if not (isinstance(item.amount, (int, float)) and item.amount >= 0):
                return "Invalid amount: %s" % item.amount
            amt = Decimal(str(item.amount))
            qty = item.quantity
            net -= amt * qty
            total_expenses += amt * qty
        else:
            return "Invalid item type: %s" % item.type

    if total_expenses > MAX_TOTAL or total_payments > MAX_TOTAL:
        return "Total amount payable for an order exceeded"

    if net != 0:
        # Use float(net) for formatting
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, float(net))
    else:
        return "Order ID: %s - Full payment received!" % order.id