public class Main {
    public static void main(String[] args) {
        ListNode l1 = ListNode.deserialize("[2,4,9]");
        ListNode l2 = ListNode.deserialize("[5,6,4,9]");


        Solution solution = new Solution();

        solution.addTwoNumbers(l1, l2).display();
    }
}
