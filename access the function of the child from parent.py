class venkat:
    def show(self):
        print("venkat")

class sashi(venkat):
    def display(self):
        print("sashi")
p1 = venkat
c1 = sashi

p1.show(venkat)
c1.display(venkat)