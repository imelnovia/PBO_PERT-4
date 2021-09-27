class baju:
    def __init__(self, merk, warna, ukuran):
        self.merk = merk
        self.warna = warna
        self.ukuran = ukuran

    def printname(self):
        print(self.merk)
        print(self.warna)
        print(self.ukuran)

class female(baju):
     def __init__(self, merk, warna, ukuran):
         baju.__init__(self, merk, warna, ukuran)
         self.harga = "Rp. 210.000"

     def female(Self):
        print("Merk       : ", Self.merk)
        print("Warna      : ", Self.warna)
        print("Ukuran     : ", Self.ukuran)
        print("Harga      : ", Self.harga)


class male(baju):
    def __init__(self, merk, warna, ukuran):
          baju.__init__(self, merk, warna, ukuran)
          self.harga = "Rp. 150.000"

    def male(Self):
        print("Merk       : ", Self.merk)
        print("Warna      : ", Self.warna)
        print("Ukuran     : ", Self.ukuran)
        print("Harga      : ", Self.harga)

x = female("Rabbani", "Hitam", "M")
y = male("Roughneck", "Hitam", "L")

x.female()
y.male()