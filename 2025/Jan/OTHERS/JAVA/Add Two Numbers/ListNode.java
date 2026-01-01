import java.math.BigInteger;

public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    ListNode(String strNumber){
        String invertedStr = revert(strNumber.strip());
        char[] chars = invertedStr.toCharArray();

        int index = 0;
        this.val = Character.getNumericValue(chars[index]);
        index++;

        ListNode tempListNode = this;
        ListNode newListNode = null;

        while (index < chars.length) {
            newListNode = new ListNode(Integer.parseInt(String.valueOf(chars[index])));

            tempListNode.next = newListNode;
            tempListNode = newListNode;
            index++;
        }

    }

    private static String revert (String s){
        String r = "";
        char ch;

        for (int i = 0; i < s.length(); i++) {
              
            ch = s.charAt(i);
          
            r = ch + r; 
        }
        return r;
    }

    public void display(){
        ListNode temp = this;
        while (temp.next != null) {
            System.out.println(temp.val+" -> ");
            temp = temp.next;
        }
        System.out.println(temp.val);
    }

    public BigInteger toNumber(){
        String revertedNumer = "";
        ListNode temp = this;

        while (temp.next != null) {
            revertedNumer += temp.val;
            temp = temp.next;
        }
        revertedNumer += temp.val;

        return new BigInteger(revert(revertedNumer));

    }


    public static ListNode deserialize(String strNumber) { 
        strNumber = strNumber.replaceAll("[^0-9]", "");
        return new ListNode(revert(strNumber));
    }
    
}