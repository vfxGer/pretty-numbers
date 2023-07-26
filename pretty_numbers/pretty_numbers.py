#!/usr/bin/env python
########################################################
__author__ = "Gerard Keating vfxger.com"
########################################################
from typing import Any, Sequence, Set
import re


def getPrettyTextFromSet(frames: Set[int]) -> str:
    """
    Given a set of integers returns a more human readable string
    """
    if not frames:
        return ""
    if len(frames) == 1:
        framesSet = frames.copy()
        return str(framesSet.pop())
    framesList = list(frames)
    framesList.sort(reverse=True)
    lastNum = framesList.pop()
    currentStrStart = lastNum
    pStr = str(lastNum)
    while framesList:
        currNum = framesList.pop()
        if not lastNum + 1 == currNum:
            if not lastNum == currentStrStart:
                pStr = pStr + "-" + str(lastNum)
            pStr = pStr + "," + str(currNum)
            currentStrStart = currNum
        lastNum = currNum
    if currentStrStart != currNum:
        pStr = pStr + "-" + str(lastNum)
    return pStr


def getPrettyTextFromNumbers(frames: Sequence[int]) -> str:
    """
    Given iterable of integers returns a more human readable string
    """
    framesSet = set(frames)
    return getPrettyTextFromSet(framesSet)


def getPrettyNumbersText(list_of_strings: Sequence[Any]) -> str:
    nums = set()
    text_result = set()
    for i in list_of_strings:
        try:
            nums.add(int(i))
        except (TypeError, ValueError):
            text_result.add(str(i))
    result = getPrettyTextFromSet(nums)
    if not text_result:
        return result
    texts = list(text_result)
    texts.sort()
    final_text = ",".join(texts)
    if result:
        return result + "," + final_text
    return final_text


def getNumbersFromText(text: str) -> Set[int]:
    """
    > getNumbersFromText("1,2,5-9")
    > {1,2,5,6,7,8,9}
    """
    range_re = re.compile(r"\s*([0-9]+)\s*-\s*([0-9]+)\s*")
    result = set()
    for unit in text.split(","):
        unit = unit.strip()
        if unit.isdigit():
            result.add(int(unit))
        else:
            reg_res = range_re.match(unit)
            if reg_res:
                r1 = int(reg_res.groups()[0])
                r2 = int(reg_res.groups()[1])
                start = min((r1, r2))
                end = max((r1, r2))
                result = result.union(set(range(start, end + 1)))
    return result
