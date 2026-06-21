class Solution(object):
    def isSymmetric(self, root):
        def mirror(l,r):
            if not l and not r:
                return True
            
            if not l or not r:
                return False

            return (l.val == r.val and 
                    mirror(l.left, r.right) and
                    mirror(l.right, r.left))

        return mirror(root.left, root.right)