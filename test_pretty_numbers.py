#!/usr/bin/env python
########################################################
__author__ = "Gerard Keating"
__date__ = "12 Feb 2013"
########################################################

import unittest

import pretty_numbers


class TestListUtils(unittest.TestCase):
    def setUp(self):
        self.compList = [
            [set([99]), "99"],
            [
                set([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]),
                "1001-1010",
            ],
            [
                set(
                    [
                        99,
                        1001,
                        1002,
                        1003,
                        1004,
                        1005,
                        1006,
                        1007,
                        1008,
                        1009,
                        1010,
                        1111,
                    ]
                ),
                "99,1001-1010,1111",
            ],
            [
                set(
                    [
                        1001,
                        1002,
                        1003,
                        1004,
                        1005,
                        1006,
                        1007,
                        1008,
                        1009,
                        1010,
                        1111,
                    ]
                ),
                "1001-1010,1111",
            ],
            [
                set([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]),
                "1001-1010",
            ],
            [set([]), ""],
        ]

    def test_no_isdigit_attribute(self):
        self.assertEqual(
            pretty_numbers.getPrettyNumbersText(["1", {1: 2}]), "1,{1: 2}"
        )

    def test_prettyTextFromSet(self):
        for set_, text in self.compList:
            self.assertEqual(pretty_numbers.getPrettyTextFromSet(set_), text)

    def test_getPrettTextFromNumbers(self):
        self.assertEqual(
            pretty_numbers.getPrettyTextFromNumbers(
                [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
            ),
            "1001-1010",
        )

    def test_getPrettyNumbersText(self):
        list_txt = [
            u"- TPB vol. 01",
            u"1",
            u"3",
            u"1",
            u"2",
            u"2",
            u"1",
            u"- HC vol. 01",
            u"3",
            u"- HC vol. 01",
            u"3",
            u"2",
            u"- TPB vol. 01",
        ]
        self.assertEqual(
            "1-3,- HC vol. 01,- TPB vol. 01",
            pretty_numbers.getPrettyNumbersText(list_txt),
        )

    def test_getPrettyNumbersText_with_ints(self):
        list_txt = [
            u"- TPB vol. 01",
            u"1",
            u"3",
            u"1",
            u"2",
            u"2",
            u"1",
            6,
            u"- HC vol. 01",
            u"3",
            u"- HC vol. 01",
            u"3",
            u"2",
            u"- TPB vol. 01",
        ]
        self.assertEqual(
            "1-3,6,- HC vol. 01,- TPB vol. 01",
            pretty_numbers.getPrettyNumbersText(list_txt),
        )
        import sys
        print(sys.version)
        assert "5" not in sys.version
