from unittest import mock, TestCase
from pricer import Pricer

class TestClassAttribute(TestCase):

	def test_instance_attribute_without_patch(self):
		pricer = Pricer()
		self.assertAlmostEqual(pricer.get_discounted_price(100), 80.0)

	def test_patch_instance_attribute(self):
		pricer = Pricer()
		pricer.DISCOUNT = 0.5
		self.assertAlmostEqual(pricer.get_discounted_price(100), 50.0)

	def test_set_class_attribute(self):
		Pricer.DISCOUNT = 0.6
		pricer = Pricer()
		self.assertAlmostEqual(pricer.get_discounted_price(100), 60.0)

	def test_patch_class_attribute(self):
		with mock.patch.object(Pricer, 'DISCOUNT', 1):
			pricer = Pricer()
			self.assertAlmostEqual(pricer.get_discounted_price(100), 100.0)

if __name__ == '__main__':

	t = TestClassAttribute()			
	t.test_instance_attribute_without_patch()
	t.test_patch_instance_attribute()
	t.test_patch_class_attribute()
