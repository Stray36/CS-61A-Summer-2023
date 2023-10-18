# Discussion 4: Mutability, Data Abstraction, Trees

# Q2: Insert Items
def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurrence of entry and then returns lst.
    Do not create any new lists.

    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> test_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> double_lst = [1, 2, 1, 2, 3, 3]
    >>> double_lst = insert_items(double_lst, 3, 4)
    >>> double_lst
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    # i = 0
    # while True:
    #     if lst[i] == None:
    #         return lst
    #     elif lst[i] == entry:
    #         lst.insert(i + 1, elem)
    #         if entry == elem:
    #             i += 1
    #     i += 1
    index = 0
    while index < len(lst):
        if lst[index] == entry:
            lst.insert(index + 1, elem)
            if entry == elem:
                index += 1
        index += 1
    return lst


# Q3: Add This Many
def add_this_many(x, el, s):
    """Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** YOUR CODE HERE ***"
    # index = 0
    # while index < len(s):
    #     if s[index] == x:
    #         s.append(el)
    #     index += 1

    for i in range(len(s)):
        if s[i] == x:
            s.append(el)

# Q5: Height
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"


# Q6: Maximum Path Sum
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"



# Q7: Find Path
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    


