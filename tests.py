import unittest
from league_ranking import main
from unittest.mock import patch
import sys
import io

class TestLeagueRanking(unittest.TestCase):

	def test_main_function(self):
		with patch("sys.argv", [None, "test_data.txt"]):
			capturedOutput = io.StringIO()
			sys.stdout = capturedOutput
			main()
			sys.stdout = sys.__stdout__
			self.assertEqual(capturedOutput.getvalue(),'1. Lions, 3 pts\n2. Snakes, 0 pts\n')
		

if __name__ == '__main__':
	unittest.main()
