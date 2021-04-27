class Field:

	def __init__(self, type_, default, value=None):
		self.type_ = type_
		self.default = default
		self._value = value		

	@property
	def value(self):
		if self._value is None:
			return self.default
		else:
			return self._value

if __name__ == '__main__':
	f = Field('Integer', 2, 5)
	print(f.value)

	g = Field('Integer', 2)
	print(g.value)
