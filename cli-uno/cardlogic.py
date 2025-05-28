CARDID: list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Block", "Reverse", "+2", "Wild", "+4 Wild"]
CARDCOLOR: list = ["Red", "Green", "Blue", "Yellow", "Black"]

class playingCard:
    def __init__(self, color, id):
        self.id = CARDID[id]
        
        if (id == 13) or (id == 14):
            color = 4

        self.color = CARDCOLOR[color]

