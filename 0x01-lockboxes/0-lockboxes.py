#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """ lock """
    if not boxes:
        return False

    visited = set()
    stack = [0]

    while stack:
        box = stack.pop()
        visited.add(box)
        keys = boxes[box]
        for key in keys:
            if key not in visited and key < len(boxes):
                stack.append(key)

    return len(visited) == len(boxes)
