def total_bill(bill_amount, tip_perc):
    total = bill_amount*(1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f'Please pay ${total}')

total_bill(150, 20)