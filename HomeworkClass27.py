class Dogs:
    species="Dog"
    def __init__(self,breed,color):
        self.breed=breed
        self.color=color
peach=Dogs("German Shepard","dark brown")
molly=Dogs("Golden Retriver","light yellow")
print("Peach is a {}".format(peach.species))
print("Molly is a {}".format(molly.species))
print("Peach is a {}".format(peach.breed,peach.color))
print("Molly is a {}".format(molly.breed,molly.color))
print("Peach is {}".format(peach.color))
print("Molly is {}".format(molly.color))