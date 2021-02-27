import os
import unittest

from sncf import Sncf

class Test(unittest.TestCase):

    def test_readJson(self):

        testClass = Sncf()
        
        testClass.readJson("journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025") 
        #self.assertTrue(os.path.exists('./my_stop_areas.csv'))
        
        self.assertTrue(os.path.exists(testClass.fileJson+".json"))
        #self.assertTrue(os.path.exists('./stop_areas_maria.json'))

    def test_getJson(self):
        testClass = Sncf()
        self.assertEqual(type(testClass.getJson()),dict)
    
    def test_combien_arrets(self):
        testClass = Sncf()
        self.assertEqual(type(testClass.combien_arrets("journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025")),int)

if __name__  == '__main__':
    unittest.main(verbosity =2)