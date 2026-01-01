public class Solution {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode temp = new ListNode(0);
        ListNode current = temp;
        int carryOver = 0;

        while (l1 != null || l2 != null || carryOver != 0) {
            int total = carryOver;

            if (l1 != null) {
            total += l1.val;
            l1 = l1.next;
            }
            if (l2 != null) {
            total += l2.val;
            l2 = l2.next;
            }

            carryOver = total / 10;
            current.next = new ListNode(total % 10);
            current = current.next;
        }
        return temp.next;
    }
}