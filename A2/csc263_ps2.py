'''
CSC263 Winter 2022
Problem Set 2 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any additional "import" statements
from math import floor
import doctest

#############################################
# Hash table
###############################################

# Placeholder for a deleted element
DELETED = "DELETED"


# Element in the HashTable
class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.value = self.val

    def __repr__(self):
        return str(self.key) + ";" + str(self.val)

    def get_k(self):
        return self.key

    def get_v(self):
        return self.val


class HashTable(object):
    """
    A hash table object. Each hash table will have the
    following fields:
        array:    The address table, represented as a list in Python.
                  The values of this address table is either None,
                  DELETED, or a Node object
        capacity: The current size of the address table
        size:     The number of elements in the table.
    """

    def __init__(self, initial_capacity=20):
        # Hash table capacity
        self.capacity = initial_capacity
        self.initial_capacity = initial_capacity

        # Initialize the address table to have all "None"
        # This table should have elements None, "DELTED", or a Node object
        self.array = [None] * initial_capacity

        # Track the number of elements in the hash table
        self.size = 0

    def hash(self, k, capacity=None):
        """
        Hash function that returns a bucket {0, 1, 2, ..., capacity-1} given
        a key `k`. The argument `capacity` is initialized to `self.capacity`,
        but an alternative capacity can be provided.

        This function is provided to you.
        """
        A = 0.45352364758429879433234
        if capacity is None:
            capacity = self.capacity
        return floor(capacity * (hash(k) * A % 1))

    def insert(self, k, v):
        """
        Insert Node(k, v) into the hash table. Use the hash function self.hash(),
        and linear probing if the slot is already occupied.

        If the key `k` already exists in the Hash Table, replace the coresponding
        value `v`.

        If the hash table capacity is above 75%, double the hash table capacity.
        """
        self.size += 1
        if self.size > float(self.capacity * 0.75):
            self.capacity = self.capacity * 2
            c = self.array[:]
            self.array = [None] * self.capacity  # build a new list
            for i in range(len(c)):             # re-add each node to the new list
                if c[i] is not None and c[i] is not DELETED:
                    k_1 = c[i].get_k()
                    v_1 = c[i].get_v()
                    self.insert_helper(k_1, v_1)
            self.insert_helper(k, v)            #add the last node
        else:
            self.insert_helper(k, v)

    def insert_helper(self, k, v):
        """
        a helper function for insert
        This function is more likely a base case for insert
        which is add the v into the hash
        k: key, which represent the place of node we are adding
        v: an element which is the value of the node we are adding to
        """
        c = self.hash(k)
        no = Node(k, v)
        if self.array[c] is None or self.array[c] is DELETED:
            self.array[c] = no
        else:
            i = 0
            c = self.hash(k, i)
            while self.array[c] is (not None and not DELETED):
                i = i + 1
                c = self.hash(k, i)
            self.array[c] = no

    def search(self, k):
        """
        Return the value of the node with key k in the hash table,
        or None if no such node exists.
        """
        k_node = self.hash(k)
        if (type(self.array[k_node]) is Node) and (self.array[k_node].get_k() == k):
            return self.array[k_node]
        else:
            i = 0
            while i < self.capacity - 1:
                k_node = self.hash(k, i)
                if (type(self.array[k_node]) is Node) and self.array[k_node].get_k() == k:
                    return self.array[k_node]
                else:
                    i += 1
            return None

    def delete(self, k):
        """
        Delete the node with key `k` from the hash table, if it exists.

        If the hash table capacity is below 25%, halve the hash table capacity,
        but do not go below self.initial_capacity
        """
        if self.search(k) is None:
            return
        else:
            self.size -= 1
            key = self.delete_helper_1(k)
            self.array[key] = DELETED
            self.delete_helper_2()

    def delete_helper_1(self, k):
        """
        A helper function for delete.
        Assume k is in one of the key of node in the HashTable
        Getting the index of node with key k in the list
        """
        k_node = self.hash(k)
        if self.array[k_node].get_k() == k:
            return k_node
        else:
            i = 0
            while i < self.capacity - 1:
                k_node = self.hash(k, i)
                if self.array[k_node].get_k() == k:
                    return k_node
                else:
                    i += 1

    def delete_helper_2(self):
        """
        A helper function for delete
        if the size is less than 25% of the capacity
        and current capacity is greater than initial capacity
        then shrink its size
        and add all current node to the new list.
        """
        if self.size < self.capacity * 0.25:
            if self.capacity > self.initial_capacity:
                self.capacity = self.capacity // 2
                c = self.array[:]
                self.array = [None] * self.capacity        # build a new list
                for i in range(len(c)):                    # re-add each node to the new list
                    if c[i] is not None and c[i] is not DELETED:
                        k_1 = c[i].get_k()
                        v_1 = c[i].get_v()
                        self.insert_helper(k_1, v_1)

    # You may write helper functions freely


# You may add additional test case below. HOWEVER, your code must
# compile and be runnable in order to earn any credit for correctness.

if __name__ == "__main__":
    T = HashTable(10)
    T.insert(1, "c")
    T.delete(1)
    # check that the DELTETED token is used
    assert T.array[T.hash(1)] == DELETED
    T.insert(1, "c")
    T.insert(2, "s")
    T.insert(3, "c")
    T.insert(4, "2")
    T.insert(5, "6")
    T.insert(6, "3")

    # check that size and capacity are tracked correctly
    assert (T.size == 6)
    assert (T.capacity == 10)

    # check that search gives us the appropriate result
    n = T.search(1)
    assert (n.value == "c")

    T = HashTable(5)
    T.insert(1, "c")
    T.delete(1)
    # check that the DELTETED token is used
    assert T.array[T.hash(1)] == DELETED
    T.insert(1, "c")
    T.insert(2, "s")
    T.insert(3, "c")
    T.insert(4, "2")
    # check if the capacity will double
    assert (T.capacity == 10)
    T.insert(5, "6")
    T.insert(6, "3")

    # check that size and capacity are tracked correctly
    assert (T.size == 6)
    assert (T.capacity == 10)

    # check that search gives us the appropriate result
    n = T.search(1)
    assert (n.value == "c")

    T.delete(1)
    T.delete(2)
    T.delete(3)
    T.delete(4)

    # check the capacity will shrink after delete
    assert (T.size == 2)
    assert (T.capacity == 5)

    a = T.array[:]
    T.delete(1)
    # check if delete a k not belong to HashTable, the array would not change
    assert (T.array == a)

    # check if the capacity would not change if capacity is equal to the initial capacity
    T.delete(5)
    assert (T.capacity == 5)

    # One rare case
    T = HashTable(1)
    T.insert(1, "c")
    assert (T.size == 1)
    assert (T.capacity == 2)
    T.delete(1)
    assert (T.size == 0)
    assert (T.capacity == 1)
    T.delete(1)
    assert (T.size == 0)
    assert (T.capacity == 1)
