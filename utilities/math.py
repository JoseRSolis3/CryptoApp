from crypto_data import get_crypto_price

current_price = get_crypto_price(crypto="pepe")
current_shares = 5000000

def percent_conv(percent):
    return percent / 100

def shares_adjust_by_percent(current_shares, percent, increase=True):
    converted_percent = percent_conv(percent)
    if increase:
        return current_shares * (1 + converted_percent)
    else:
        return current_shares * (1 - converted_percent)
    
def price_adjust_by_percent(current_price, percent, increase=True):
    converted_percent = percent_conv(percent)
    if increase:
        return current_price * (1 + converted_percent)
    else:
        return current_price * (1 - converted_percent)
    
def sixty_twenty_ten_ten(current_shares):
    sixty_percent = current_shares * percent_conv(60)
    twenty_percent = current_shares * percent_conv(20)
    ten_percent = current_shares * percent_conv(10)

    return {
        "60% - Primary" : sixty_percent,
        "20% - Secondary" : twenty_percent,
        "10% - flexible" : ten_percent,
        "10% - hold" : ten_percent
    }

def fifty_thirty_twenty(current_shares):
    result = {}

    percentages = [50, 30, 20]

    for percent in percentages:
        percentage = percent_conv(percent)
        split_shares = int(round(current_shares * percentage))
        result[f"{percent}%"] = split_shares
    return result

def fourway_split(current_price, current_shares, buy):
    result = {}

    twentyfive_percent = current_shares * percent_conv(25)

    for i in range(1, 5):
        adjusted_price = price_adjust_by_percent(current_price, i, not buy)
        formatted_price = format_price(adjusted_price)
        shares_sold = int(round(twentyfive_percent / adjusted_price))
        result[f"25% at {formatted_price}"] = shares_sold
    return result

def tenway_split(current_price, current_shares, buy):
    result = {}

    ten_percent = current_shares * percent_conv(10)

    for i in range(1, 11):
        adjusted_price = price_adjust_by_percent(current_price, i, not buy)
        formatted_price = format_price(adjusted_price)
        split_shares = int(round(ten_percent / adjusted_price))
        result[f"10% at {formatted_price}"] = split_shares
    return result

def format_price(price):
    formatted_price = "{:.20f}".format(price).rstrip('0').rstrip('.')
    return formatted_price

print(current_price)
print(format_price(current_price))
print(fourway_split(current_price, current_shares, buy=False))
print(fifty_thirty_twenty(current_shares))
print(sixty_twenty_ten_ten(current_shares))