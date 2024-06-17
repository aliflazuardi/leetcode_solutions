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

// solution using fast and slow pointers
/* class Solution { */
/* public: */
/*     bool hasCycle(ListNode* head) { */
/*         ListNode* fast = head; */
/*         ListNode* slow = head; */
/**/
/*         while (fast != NULL && fast->next != NULL) { */
/*             fast = fast->next->next; */
/*             slow = slow->next; */
/**/
/*             if (fast == slow) { */
/*                 return true; */
/*             } */
/*         } */
/**/
/*         return false; */
/*     } */
/* }; */

