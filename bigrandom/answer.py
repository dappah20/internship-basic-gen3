class BigRandom:
    def __init__(self):
        self.data = "data.txt"
        # add attributes if you need more

    def answer(self):
        noh, suc = 0, 0
        nom = ''.join([str(x) for x in range(10000)])
        for line in self.data.readline():
            noh = 0
            suc = 0 

        # your algorithm

        return (noh - 10000 ,suc - (ord('#') * 10000 + sum([ord(x) for x in nom])))

    # add methods if you need more
