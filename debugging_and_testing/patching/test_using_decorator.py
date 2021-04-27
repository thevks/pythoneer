from unittest import TestCase, mock
from work import work_on

@mock.patch('work.os')
def test_using_decorator(self, mocked_os):
	work_on()
	mocked_os.getcwd.assert_called_once()

if __name__ == '__main__':
	with mock.patch('work.os') as mocked_os:
		test_using_decorator(mocked_os)
