from xmlrpc.server import SimpleXMLRPCServer

def add(x,y):
	return x+y

class KeyValueServer:
	_rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']

	def __init__(self, server):
		self._data = {}
		for name in self._rpc_methods_:
			server.register_function(getattr(self, name))
	
	def get(self, name):
		return self._data[name]

	def set(self, name, value):
		self._data[name] = value

	def delete(self, name):
		del self._data[name]

	def exists(self, name):
		return name in self._data

	def keys(self):
		return list(self._data)


if __name__ == '__main__':

	server = SimpleXMLRPCServer(('', 16000), allow_none=True)
	server.register_function(add)
	kvserv = KeyValueServer(server)
	server.serve_forever()
