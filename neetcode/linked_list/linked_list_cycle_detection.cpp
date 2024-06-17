/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// solution using set
class Solution {
public:
    bool hasCycle(ListNode* head) {
        set<ListNode*> pointers;

        while(head->next != NULL) {
            if (pointers.count(head) == 1) {
                return true;
            }
            pointers.insert(head);
            head = head->next;
        }

        return false;
    }
}
