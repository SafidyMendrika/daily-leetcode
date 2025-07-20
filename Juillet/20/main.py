from collections import defaultdict

class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        tree = {}
        for path in paths:
            node = tree
            for folder in path:
                node = node.setdefault(folder, {})
        
        duplicates = defaultdict(list)
        
        def serialize(node):
            if not node:
                return "()"
            children_serialization = "".join(child + serialize(child_node) for child, child_node in sorted(node.items()))
            serial = "(" + children_serialization + ")"
            duplicates[serial].append(node)
            return serial
        
        serialize(tree)
        
        for nodes in duplicates.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.clear()      
                    node["#"] = True 
        
        ans = []
        def collect_paths(node, path):
            for child_name, child_node in node.items():
                if "#" in child_node:
                    continue
                new_path = path + [child_name]
                ans.append(new_path)
                collect_paths(child_node, new_path)
        
        collect_paths(tree, [])
        return ans
    
solution = Solution()
paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
print(solution.deleteDuplicateFolder(paths))