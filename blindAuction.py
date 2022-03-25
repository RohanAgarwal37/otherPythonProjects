from turtle import clear


def find_highest(bid_dict):
    highest_bid = 0
    winner = ""
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


next_bidder = True
bid_dict = {}
while next_bidder:
    bidder_name = input("Enter your name please ")
    bid = int(input("Please enter your Bid $"))
    bid_dict[bidder_name] = bid
    cont = input("Is there a next bidder type 'yes' or 'no' ")
    if cont == "no":
        next_bidder = False
        find_highest(bid_dict)
    elif cont == "yes":
        clear()
