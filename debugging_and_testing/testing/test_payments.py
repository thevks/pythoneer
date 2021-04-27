import pytest

@pytest.mark.client_a
def w():
	pass

@pytest.mark.client_a
@pytest.mark.client_b
def m():
	pass

@pytest.mark.client_b
def n():
	pass
