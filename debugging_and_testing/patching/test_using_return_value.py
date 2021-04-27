from unittest import TestCase, mock
from work import work_on

def test_using_return_value():
	with mock.patch('work.os.getcwd', return_value='testing'):
		assert work_on() == 'testing'

if __name__ == '__main__':
	test_using_return_value()
