
from typing import List


class TreeNode:
    """
    A tree node has pointer and key pairs
    The last entry is a pointer to next node
    """
    MAX_NODE_SIZE = 3
    
    data: List

    is_leaf: bool


    def __init__(self) -> None:
        pass

    def insert(self, value) -> None:
        is_present, node = self.find(value)

        if is_present:
            raise ValueError('Key is already present. This implementation does not support duplicates')
        
        else:
            curr_len = len(self.data)
            expected_len_after_addition = curr_len + 2 # one for pointer, other for data
            if expected_len_after_addition >= TreeNode.MAX_NODE_SIZE:
                # we need to split
                # split
                pass

            else:
                # we can go ahead and insert
                for i in range(1, len(self.data), 2):
                    if self.data[i] <= value:
                        self.data.insert(i, value) # key
                        self.data.insert(i, value) # value



    def find(self, value) -> None:
        """
        Finding a value is iterating over the data and finding out the correct

        Returns:
            the pointer and the node where it was found
            None if not found and the last node where it should have been
        """
        if self.is_leaf:
            for i in range(1, len(self.data), 2):
                if self.data[i] == value:
                    return self.data[i-1], self
            return None, self
        else:
            for i in range(1, len(self.data), 2):
                if self.data[i] <= value:
                    return self.find(value)
        


class BTree:
    root: TreeNode
    
    def __init__(self) -> None:
        root = TreeNode()

    def insert(self, value) -> None:
        pass

    def find(self, value):
        pass



if __name__ == '__main__':
    print('Hello')