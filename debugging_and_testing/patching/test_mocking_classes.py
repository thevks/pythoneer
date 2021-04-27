from unittest import TestCase, mock
from worker import Worker, Helper

class TestWorkerModule(TestCase):

	def test_patching_class(self):
		with mock.patch('worker.Helper', autospec = True) as MockHelper:
			MockHelper.return_value.get_path.return_value = 'testing'
			worker = Worker()
			MockHelper.assert_called_once_with('/tmp')
			self.assertEqual(worker.work(), 'testing')

	def test_partial_patching(self):
		with mock.patch.object(worker.Helper, 'get_path', return_value = 'testing'):
			worker = Worker()
			self.assertEqual(worker.helper.path, '/tmp')
			self.assertEqual(worker.work(), 'testing')
			

if __name__ == '__main__':
	t = TestWorkerModule()
	t.test_patching_class()	
	t.test_partial_patching()
