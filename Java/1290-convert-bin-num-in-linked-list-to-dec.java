/**
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode () {}
 * ListNode (int val) { this.val = val; }
 * ListNode (int val, ListNode next) { this.val = val; this.next = next }
 * }
 **/

class Solution {
    public int getDecimalValue(ListNode head) {
        // String num = "" + head.val;
        int num = head.val;
        while (head.next != null){
            // num += head.next.val;
            // num = num * 2 + head.next.val;
            num = num << 1 | head.next.val;
            head = head.next;
        }
        // return Integer.parseInt(num,2);
        return num;
    }
}
