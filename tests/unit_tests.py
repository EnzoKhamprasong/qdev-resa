import unittest
from resa.resa import *

class ResaUnitTests(unittest.TestCase):
  def test_bookMeetingRoom(self):
    self.assertEqual(bookMeetingRoom(3).__str__(), "Small")
    self.assertEqual(bookMeetingRoom(15).__str__(), "Medium")
    self.assertEqual(bookMeetingRoom(35).__str__(), "Large")
    self.assertEqual(bookMeetingRoom(212).__str__(), "Refused")

if __name__ == '__main__':
  unittest.main()
