#!/usr/bin/env python
########################################################
__author__ = "Gerard Keating"
__date__ = "12 Feb 2013"
########################################################

def getPrettyTextFromSet(frames):
    """
    Given a set of integers returns a more human readable string
    """
    if not frames: 
        return ""
    if len(frames)==1:
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

def getPrettyTextFromNumbers(frames):
    """
    Given iterable of integers returns a more human readable string
    """
    framesSet = set(frames)
    return getPrettyTextFromSet(framesSet)
