import unittest
from controller import count_vote

class MyTestCase(unittest.TestCase):
    def test_count_vote(self):
        #try different people
        self.assertEqual(count_vote(['Jane','Doe','555 Main Street','10349'], 0),
                         'You already voted!')  #someone that already voted
        self.assertEqual(count_vote(['Jane','Doe','555 Main Street','10341'], 0),
                         'Voter isn\'t registered or voter info is incorrect')  #voter doesn't exist or typed in incorrect info

        #someone who doesn't click the voting box the first time
        self.assertEqual(count_vote(['John', 'Doe', '555 Main Street', '34930'], 0),
                         'Please select someone to vote for')
        self.assertEqual(count_vote(['John', 'Doe', '555 Main Street', '34930'], 0),
                         'Please select someone to vote for')
        self.assertEqual(count_vote(['John', 'Doe', '555 Main Street', '34930'], 1),
                         'You voted for John Doe')

        #Trying to vote twice
        self.assertEqual(count_vote(['Drew', 'Nelson', '1234 Hickory Lane', '58943'], 1),
                         'You voted for John Doe')
        self.assertEqual(count_vote(['Drew', 'Nelson', '1234 Hickory Lane', '58943'], 1),
                         'You already voted!')



if __name__ == '__main__':
    unittest.main()
