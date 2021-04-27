import os

class Helper:
	def __init__(self, path):
		self.path = path
	def get_path(self):
		base_path = os.getcwd()
		return base_path.join(self.path) 

class Worker:
	def __init__(self):
		self.helper = Helper('/tmp')
	
	def work(self):
		path = self.helper.get_path()
		print(path)

if __name__ == '__main__':
	w = Worker()
	w.work()
