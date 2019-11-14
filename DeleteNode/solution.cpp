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
    void deleteNode(ListNode* node) {
        ListNode * prev = NULL;
        while (node->next){
            prev = node;
            node->val = node->next->val;
            node = node->next;
        }
        prev->next = NULL;
    }
};
// Runtime: 12 ms, faster than 80.48% of C++ online submissions for Delete Node in a Linked List.
// Memory Usage: 9.3 MB, less than 84.62% of C++ online submissions for Delete Node in a Linked List.