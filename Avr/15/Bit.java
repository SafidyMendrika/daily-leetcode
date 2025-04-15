public class Bit {
    int[] tree;
    
    public Bit(int n) {
        tree = new int[n + 1];
    }
    
    public void update(int idx, int val) {
        idx++; 
        while (idx < tree.length) {
            tree[idx] += val;
            idx += idx & -idx;
        }
    }
    
    public int query(int idx) {
        idx++; 
        int sum = 0;
        while (idx > 0) {
            sum += tree[idx];
            idx -= idx & -idx; 
        }
        return sum;
    }
}