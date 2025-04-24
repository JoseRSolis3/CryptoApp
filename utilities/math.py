from crypto_data import get_crypto_price

current_price = get_crypto_price(crypto="pepe")
current_shares = 5000000

def alphabet_list():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return list(alphabet)

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
        split_price = int(round(ten_percent / adjusted_price))
        result[f"10% at {formatted_price}"] = split_price
    return result

def split(percentages, current_shares):
    result = {}
    i = 0
    letters = alphabet_list()        
    for percent in percentages:
        percentage = percent_conv(percent) 
        split_share = int(round(current_shares * percentage))
        if f"{percent}.{letters[i]}%" in result:
            i += 1
            result[f"{percent}.{letters[i]}%"] = split_share
        else:
            result[f"{percent}.{letters[i]}%"] =  split_share
            i = 0
    return result

def eighty_ten_ten(current_shares):
    percentages = [80, 10, 10]
    return split(percentages)


def seventyfive_twentyfive_twentyfive(current_shares):
    percentages = [75, 25, 25]
    return split(percentages)

def ninety_five_five(current_shares):
    percentages = [90, 5, 5]
    return split(percentages)

def forty_thirty_thirty():
    percentages = [40, 30, 30]
    return split(percentages)

def sixty_fourtens():
    percentages = [60, 10, 10, 10, 10]
    return split(percentages)

def twothirty_twotwenty():
    percentages = [30, 30, 20, 20]
    return split(percentages)

def three_way():
    percentages = [33, 33, 33, 1]
    return split(percentages)

def sixty_thirty_ten():
    percentages = [60, 30, 10]
    return split(percentages)

def seventyfive_fifteen_twofive():
    percentages = [75, 15, 5, 5]
    return split(percentages)

def format_price(price):
    formatted_price = "{:.20f}".format(price).rstrip('0').rstrip('.')
    return formatted_price

print(eighty_ten_ten(current_shares=100))