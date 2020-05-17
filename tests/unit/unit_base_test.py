# Create this unit_base_test to avoid having to import app as unused import
# above every unit test we make


from app import app
from unittest import TestCase

class UnitBaseTest(TestCase):
    pass

