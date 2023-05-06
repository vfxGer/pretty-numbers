#!/usr/bin/env python
########################################################
__author__ = "Gerard Keating"
__date__ = "12 Feb 2013"
########################################################

import unittest
from typing import Any, List

import pretty_numbers


class TestListUtils(unittest.TestCase):
    compList: List[Any]

    def setUp(self) -> None:
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

    def test_no_isdigit_attribute(self) -> None:
        self.assertEqual(
            pretty_numbers.getPrettyNumbersText(["1", {1: 2}]), "1,{1: 2}"
        )

    def test_prettyTextFromSet(self) -> None:
        for set_, text in self.compList:
            self.assertEqual(pretty_numbers.getPrettyTextFromSet(set_), text)

    def test_getPrettTextFromNumbers(self) -> None:
        self.assertEqual(
            pretty_numbers.getPrettyTextFromNumbers(
                [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
            ),
            "1001-1010",
        )

    def test_getPrettyNumbersText(self) -> None:
        list_txt = [
            "- TPB vol. 01",
            "1",
            "3",
            "1",
            "2",
            "2",
            "1",
            "- HC vol. 01",
            "3",
            "- HC vol. 01",
            "3",
            "2",
            "- TPB vol. 01",
        ]
        self.assertEqual(
            "1-3,- HC vol. 01,- TPB vol. 01",
            pretty_numbers.getPrettyNumbersText(list_txt),
        )

    def test_getPrettyNumbersText_with_ints(self) -> None:
        list_txt = [
            "- TPB vol. 01",
            "1",
            "3",
            "1",
            "2",
            "2",
            "1",
            6,
            "- HC vol. 01",
            "3",
            "- HC vol. 01",
            "3",
            "2",
            "- TPB vol. 01",
        ]
        self.assertEqual(
            "1-3,6,- HC vol. 01,- TPB vol. 01",
            pretty_numbers.getPrettyNumbersText(list_txt),
        )
