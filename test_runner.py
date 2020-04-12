# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:28:36 2020

@author: david
"""

def testRunnerRegistersResult(self):
        class Test(unittest.TestCase):
            def testFoo(self):
                pass
        originalRegisterResult = unittest.runner.registerResult
        def cleanup():
            unittest.runner.registerResult = originalRegisterResult
        self.addCleanup(cleanup)

        result = unittest.TestResult()
        runner = unittest.TextTestRunner(stream=StringIO())
        # Use our result object
        runner._makeResult = lambda: result

        self.wasRegistered = 0
        def fakeRegisterResult(thisResult):
            self.wasRegistered += 1
            self.assertEqual(thisResult, result)
        unittest.runner.registerResult = fakeRegisterResult

        runner.run(unittest.TestSuite())
        self.assertEqual(self.wasRegistered, 1) 
        
        def test_startTestRun_stopTestRun_called(self):
        class LoggingTextResult(LoggingResult):
            separator2 = ''
            def printErrors(self):
                pass

        class LoggingRunner(unittest.TextTestRunner):
            def __init__(self, events):
                super(LoggingRunner, self).__init__(StringIO())
                self._events = events

            def _makeResult(self):
                return LoggingTextResult(self._events)

        events = []
        runner = LoggingRunner(events)
        runner.run(unittest.TestSuite())
        expected = ['startTestRun', 'stopTestRun']
        self.assertEqual(events, expected) 