import michaelpy
import unittest

class TestHello(unittest.TestCase):

  def test_servus(self):
    name = "Hias"
    greating = michaelpy.servus(name)
    self.assertIsInstance(greating, str)
    self.assertIn("Servus", greating)