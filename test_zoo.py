import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
   
    # Add your additional test cases here.
    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12.5), 50)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20.5), 150)

    def test_before_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60.5), 100)

    def test_born_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        
    def test_before_born(self):
        self.assertEqual(self.zoo.get_ticket_price(-1),0)

if __name__ == '__main__':
    unittest.main()