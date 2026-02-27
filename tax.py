TAX_RATE=0.06 

def cal_tax(total):
    return round(total * TAX_RATE, 2)

def cal_total_tax(total):
    tax=cal_tax(total)
    return round(total + tax, 2)