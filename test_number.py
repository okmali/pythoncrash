import unittest
from name_function import get_formatted_name

class TestNameFunction(unittest.TestCase):
    def test_formatname(self):
        formattedName=get_formatted_name("janis","joplin")
        self.assertEqual(formattedName,"Janis Joplin")

    def test_formatname2(self):
        formattedName=get_formatted_name("mehmet","ok","ali")
        self.assertEqual(formattedName,"Mehmet Ali Ok")

unittest.main()

