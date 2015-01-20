import unittest2


class TestUser(unittest2.TestCase):
    def setUp(self):
        self.name = "name"

    def tearDown(self):
        self.name = None

    def test_should_a_string(self):
        self.assertEqual(self.name, "name")
