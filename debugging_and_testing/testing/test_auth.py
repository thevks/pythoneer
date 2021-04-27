import pytest

@pytest.mark.client_a
def x():
	pass

@pytest.mark.client_b
def y():
	pass
