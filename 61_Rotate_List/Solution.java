/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || head.next == null) {
            return head;
        }

        ListNode temp = head;
        int cnt = 1;

        while(temp.next != null) {
            temp = temp.next;
            cnt++;
        }

        k = k % cnt;
        
        ListNode currHead = head;
        for(int i = 0; i < k; i++) {
            ListNode curr = currHead;
            ListNode last = null;
            while(curr.next != null) {
                last = curr;
                curr = curr.next;
            }
            curr.next = currHead;
            last.next = null;
            currHead = curr;
        }

        return currHead;
    }
}