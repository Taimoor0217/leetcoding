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
    ListNode* reverseList(ListNode* head) {
        if (head){
            ListNode* prev = NULL;
            while (head->next){
                ListNode* temp = head->next ;
                head->next = prev;
                prev = head;
                head = temp;
            }
            head->next = prev;
        }
        return head;
    }
};
// Runtime: 8 ms, faster than 77.58% of C++ online submissions for Reverse Linked List.
// Memory Usage: 9 MB, less than 100.00% of C++ online submissions for Reverse Linked List.