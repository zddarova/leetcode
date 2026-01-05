def calculate_years(principal, interest, tax, desired):
    y = 0
    while principal < desired:
        y += 1
        before_taxes = principal * interest
        after_taxes = before_taxes - before_taxes * tax
        principal += after_taxes

    return y


assert calculate_years(1000, 0.05, 0.18, 1100) == 3
assert calculate_years(1000, 0.01625, 0.18, 1200) == 14
assert calculate_years(1000, 0.05, 0.18, 1000) == 0
