import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question="what language did you first learn to speak?"
        self.responses=['English','Spanish','Dutch']
        self.my_survey=AnonymousSurvey(question)

    def test_singleResponse(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English',self.my_survey.responses)

    def test_multipleResponses(self):

        for response in self.responses:
            self.my_survey.store_response(response)        
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()