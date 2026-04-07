# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        
        node = None
        
        p_found = False
        
        q_found = False
        
        # split = False
        
        # first_found = lambda : p_found and q_found
        # p , q = p , q if p.val < q.val else q , p

        p , q = sorted([p,q], key = lambda x : x.val)
        graph = defaultdict(list)

        def dfs(r):

            nonlocal p_found , q_found , node, p, q

            if not r:
                return

            split = False
            
            if p.val <= r.val <= q.val:
                split = True
            
            if p.val == r.val:
                p_found = True
                
            if q.val == r.val:
                q_found = True

            # print(f"node name {r.val} is_split {split} p_found {p.val} {p_found} q_found {q.val} {q_found}")
             
            dfs(r.left)
            
            dfs(r.right)
            # print(f"node name {r.val} is_split {split} p_found {p.val} {p_found} q_found {q.val} {q_found}")
            
            if split and p_found and q_found :
                node = r

            return

        dfs(root)

            
            
        return node
            