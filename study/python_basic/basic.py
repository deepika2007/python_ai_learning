class make_store():
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level 

    def sip(self):
        print("Sipping chai with sweetness level:", self.sweetness, "and milk level:", self.milk_level)


chai1 = make_store("high", "full")
chai1.sip() 