class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # return self.recursive(root, p, q)
        # return self.iterative(root, p, q)
        return self.iterativePostorder(root, p, q)
    
    def recursive(self, root, p, q):
        self.res = None
        def helper(node):
            if not node: return False

            left = helper(node.left)
            right = helper(node.right)
            mid = node == p or node == q

            if left + right + mid >= 2: self.res = node

            return left or right or mid

        helper(root)
        return self.res
    
    def iterative(self, root, p, q):
        stk = [root]
        parent = {root: None}

        while p not in parent or q not in parent:
            node = stk.pop()
            if node.left:
                parent[node.left] = node
                stk.append(node.left)
            if node.right:
                parent[node.right] = node
                stk.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors: q = parent[q]

        return q
    
    def iterativePostorder(self, root, p, q):
        new, leftDone, rightDone = 0, 1, 2
        res, stk, oneNodeFound, lcaIndex = 0, [(root, new)], False, -1

        while stk:
            node, status = stk[-1]
            if status == rightDone:
                if oneNodeFound and lcaIndex == len(stk) - 1: lcaIndex -= 1
                stk.pop()
            else:
                if status == new:
                    if node == p or node == q:
                        if oneNodeFound:
                            res = stk[lcaIndex][0]
                            break
                        oneNodeFound = True
                        lcaIndex = len(stk) - 1
                stk[-1] = (stk[-1][0], stk[-1][1] + 1)
                nextNode = [node.left, node.right][status]
                if nextNode: stk.append((nextNode, new))

        return res            
