import java.util.LinkedList;
import java.util.Queue;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private class Pair {
        int height;
        TreeNode node;
        
        Pair(int height, TreeNode node) {
            this.height = height;
            this.node = node;
        }
    }
    
    public TreeNode lcaDeepestLeaves(TreeNode root) {
        if (root == null) {
            return null;
        }
        
        return findLCA(root).node;
    }
    
    private Pair findLCA(TreeNode root) {
        if (root == null) {
            return new Pair(0, null);
        }
        
        Pair left = findLCA(root.left);
        Pair right = findLCA(root.right);
        
        if (left.height == right.height) {
            return new Pair(left.height + 1, root);
        } 
        else if (left.height > right.height) {
            return new Pair(left.height + 1, left.node);
        } 
        else {
            return new Pair(right.height + 1, right.node);
        }
    }

    public static TreeNode arrayToTree(Integer[] array) {
        if (array == null || array.length == 0 || array[0] == null) {
            return null;
        }
        
        TreeNode root = new TreeNode(array[0]);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        int i = 1;
        while (!queue.isEmpty() && i < array.length) {
            TreeNode current = queue.poll();
            
            if (i < array.length) {
                if (array[i] != null) {
                    current.left = new TreeNode(array[i]);
                    queue.offer(current.left);
                }
                i++;
            }
            
            if (i < array.length) {
                if (array[i] != null) {
                    current.right = new TreeNode(array[i]);
                    queue.offer(current.right);
                }
                i++;
            }
        }
        
        return root;
    }
    public static void printLevelOrder(TreeNode root) {
        if (root == null) {
            System.out.println("[]");
            return;
        }
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        System.out.print("[");
        
        boolean first = true;
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode current = queue.poll();
                
                if (!first) {
                    System.out.print(", ");
                }
                first = false;
                
                if (current != null) {
                    System.out.print(current.val);
                    queue.offer(current.left);
                    queue.offer(current.right);
                } else {
                    System.out.print("null");
                }
            }
        }
        
        System.out.println("]");
    }
}