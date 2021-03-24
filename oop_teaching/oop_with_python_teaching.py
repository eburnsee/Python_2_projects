class Tree:
	# class attribute
	classification = "perrenial plant"
	# init method initializes data assigned to created object
	def __init__(self, species, height, age):
		# instance variables/attributes validation
		if isinstance(height, int) is False:
			raise ValueError("height must be an integer")
		if isinstance(age, int) is False:
			raise ValueError("age must be an integer")
		# instance variables/attributes
		self.species = species
		self.height = height
		self.age = age
	# print representation of object
	def __str__(self):
		return f'Tree species is {self.species}, its height is {self.height} feet, and its age is {self.age} years.'
	# data representation of object
	def __repr__(self):
		return f'Tree(species={self.species}, height={self.height} feet, age={self.age} years)'
	# function for increasing the height of the tree
	def grow_tree(self, growth_multiplier):
		return self.height*growth_multiplier
		

# making some instantiations
tree_1 = Tree('white pine', 300, 43)
tree_2 = Tree('maple', 125, 35)

# print the string respresentations of the objects
print(f'\n{tree_1}\n{tree_2}\n')
# print an class variable
print(tree_1.classification)
# print an object variable
print(tree_2.height)
# call the grow method on white_pine
print(tree_1.grow_tree(10))
# call the grow method 2
print(f'{Tree.grow_tree(tree_2, 10)} \n')		

# inheritance
# shrub is child class of parent class tree
class Shrubery(Tree):
	size = "small to medium"
	def cut_down(self):
		return f'{self.species} height is {self.height*0}'

tree_3 = Shrubery("birch", 7, 15)
# # tree 3 inherits the attributes of the tree class
# print(tree_3.species, tree_3.age)

# polymorphism
class Bush:
	classification = "more of a gardening term"
	def __init__(self, species, height):
		self.species = species
		self.height = height
	def cut_down(self):
		return f'{self.species} height is {self.height*0} \n'

tree_4 = Bush('oleander', 3)

# common function
def cut_height(plant):
	return plant.cut_down()

print(cut_height(tree_3))
print(cut_height(tree_4))