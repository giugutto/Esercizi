class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def symmetric(tree: list[int]) -> bool:
    if tree[1] != tree[2]:
        False

    else:
        if tree[3] == tree[6] and tree[4] == tree[5]:
            return True
        else:
            return False
        

