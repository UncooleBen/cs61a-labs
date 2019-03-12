""" Optional Questions for Lab 07 """

from lab07 import *

def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    stored_nodes = []
    while (link):
        if (link in stored_nodes):
            return True
        else:
            stored_nodes.append(link)
            link = link.rest
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    fast = link
    slow = link
    while fast and slow and fast.rest:
        fast = fast.rest.rest
        slow = slow.rest
        if (fast==slow):
            return True
    return False
            
        

def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def rev(t, other=True):
        if (t.is_leaf()):
            return
        l = len(t.branches)
        for i in range(l):
            rev(t.branches[i], not other)
            if (other and i<=l/2-1):
                #print("DEBUG:", t.branches[i].label, t.branches[l-1-i].label)
                t.branches[i].label, t.branches[l-1-i].label = t.branches[l-i-1].label, t.branches[i].label
        return
    return rev(t)
