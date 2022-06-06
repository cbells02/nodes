class Node1:

    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    def set_link_node(self, link_node):
        self.link_node = link_node

###objects will point to video game sequals.


Game1 = Node1("Sonic 1")
Game2 = Node1("Sonic 2")
Game3 = Node1("Sonic 3")
Game4 = Node1("Sonic Adventure")

Game1.set_link_node(Game2)
Game2.set_link_node(Game3)
Game3.set_link_node(Game4)


Game1_next = Game1.get_link_node().get_value()
Game2_next = Game2.get_link_node().get_value()
Game3_next = Game3.get_link_node().get_value()


print("Sonic 1's sequel is " + Game1_next)
print("Sonic 2's sequel is" + Game2_next)
print("Sonic 3's sequel is" + Game3_next)




