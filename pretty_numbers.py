#!/usr/bin/env python
########################################################
__author__ = "Gerard Keating vfxger.com"
########################################################
from typing import Any, Sequence, Set


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
            is_digit = i.isdigit()
        except AttributeError:
            is_digit = True
        if is_digit:
            try:
                nums.add(int(i))
            except TypeError:
                text_result.add(str(i))
        else:
            text_result.add(i)
    result = getPrettyTextFromSet(nums)
    if not text_result:
        return result
    texts = list(text_result)
    texts.sort()
    final_text = ",".join(texts)
    if result:
        return result + "," + final_text
    return final_text
