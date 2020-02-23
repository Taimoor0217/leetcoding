/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int count = 0;
        ListNode* temp = head;
        ListNode* temp1 = head;
        while(count != n){
            temp1 = temp1->next;
            count++;
        }
        if (! temp1){
            return head->next;
        }
        while(temp1->next != NULL){
            temp1 = temp1->next;
            temp = temp->next;
        }
        temp->next = temp->next->next;
        return head;
    }
};

// Runtime: 8 ms, faster than 45.15% of C++ online submissions for Remove Nth Node From End of List.
// Memory Usage: 8.9 MB, less than 5.26% of C++ online submissions for Remove Nth Node From End of List.
