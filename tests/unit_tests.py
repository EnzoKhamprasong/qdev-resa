import unittest
from resa.resa import *

class ResaUnitTests(unittest.TestCase):
  def test_bookMeetingRoom(self):
    self.assertEqual(bookMeetingRoom(3), "Small")
    self.assertEqual(bookMeetingRoom(15), "Medium")
    self.assertEqual(bookMeetingRoom(35), "Large")
    self.assertEqual(bookMeetingRoom(212), "Refused")

if __name__ == '__main__':
  unittest.main()
