class Room:
	def __init__(self, name, length, width):
		self.name = name
		self.length = length
		self.width = width
		self.square_feet = self.length * self.width

class House:
	def __init__(self, name, style):
		self.name = name
		self.style = style
		self.rooms = list()

	@property
	def living_space_footage(self):
		return sum(r.square_feet for r in self.rooms)

	def add_room(self, room):
		self.rooms.append(room)

	def __str__(self):
		return '{}: {} square foot {}'.format(self.name,self.living_space_footage, self.style)

	def __eq__(self, other):
		return self.living_space_footage == other.living_space_footage

	def __lt__(self, other):
		return self.living_space_footage < other.living_space_footage

	def __gt__(self, other):
		return self.living_space_footage > other.living_space_footage

if __name__ == '__main__':

	h1 = House('JP', 'APT')
	h1.add_room(Room('MBR', 14, 16))
	h1.add_room(Room('GBR', 12, 14))
	h1.add_room(Room('CBR', 10, 12))


	h2 = House('AP', 'APT')
	h2.add_room(Room('MBR', 13, 16))
	h2.add_room(Room('GBR', 14, 14))
	h2.add_room(Room('CBR', 9, 12))

	print(h1)
	print(h2)

	print(h1 < h2)
	print(h1 == h2)
	print(h1 > h2)
