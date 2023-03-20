from art import logo


print(logo)

Bidder_list = []
bid_again = False

while not bid_again:
    # ---------------------------------------------------------------------------------------------------------------------------
    bider_name = input("What is your name ?\n:- ")

    wrong_input = False

    while not wrong_input:
        bid_amount = input("Enter the Bid Amount ?\n:- ")
        if bid_amount.isdigit():
            new_amount = int(bid_amount)
            wrong_input = True
        else:
            print("Enter amount in Number")
            wrong_input = False

    Other_bid = input("Is there any other Person who wants to bid? Y or N:- \n").lower()
    bid_info = {}

    def auction(name, bid):

        bid_info["Name"] = name
        bid_info["Bid_amount"] = bid
        Bidder_list.append(bid_info)

    auction(name=bider_name, bid=new_amount)

    def Highest_bid(BidINfos):
        highest = 0
        person = ""
        for bidder in BidINfos:
            Bid_amount12 = BidINfos[bidder]
            if type(Bid_amount12) is int:
                Bid_amou = Bid_amount12
                if Bid_amou >= highest:
                    highest = Bid_amou
        print(f"The Winner is  Bided the Highest amount Rs:-{highest}")
    Highest_bid(BidINfos=bid_info)

    wrong_choice = False
    while not wrong_choice:
        if Other_bid == "y":
            bid_again = False
            wrong_choice = True
        elif Other_bid == "n":
            bid_again = True
            wrong_choice = True
        else:
            wrong_choice = False
            print("Wrong Choice Choose Y or N. ")