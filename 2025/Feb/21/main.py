class FindElements(object):
    def __init__(self, root):

        self.values = set()  
        
        def recover(node, value):
            if not node:
                return
            
            node.val = value
            self.values.add(value)
            
            recover(node.left, 2 * value + 1)
            recover(node.right, 2 * value + 2)
        
        recover(root, 0)

    def find(self, target):
        return target in self.values
    
