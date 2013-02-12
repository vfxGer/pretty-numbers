#!/usr/bin/env python
########################################################
__author__ = "Gerard Keating"
__date__ = "12 Feb 2013"
########################################################

import unittest

import pretty_numbers

class TestListUtils(unittest.TestCase):
    def setUp(self):
        self.compList = [[set([99]), "99"],
                         [set([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]), "1001-1010"],
                        [set([99, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1111]), "99,1001-1010,1111"],
                        [set([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1111]),"1001-1010,1111"],
                        [set([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]), "1001-1010"],
                        [set([]), ""]
                        ]
        
    def test_prettyTextFromSet(self):
        for set_, text in self.compList:
            self.assertEqual(pretty_numbers.getPrettyTextFromSet(set_), text)
            
def main():
    unittest.main()
    
if __name__ == "__main__":
    main()
    
