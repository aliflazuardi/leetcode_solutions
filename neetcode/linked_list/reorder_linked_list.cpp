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

class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* slowP = head;
        ListNode* fastP = head;

        while(fastP->next != nullptr || fast != nullptr) {
            slowP = slowP->next;
            fastP = fastP->next->next;
        }

        ListNode* second = slow->next;
    }
};

