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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* Head = new ListNode(0);
        ListNode* temp = new ListNode(0);
        ListNode* LAST = new ListNode(0); 
        int carry = 0;
        
        temp = Head;
        while(1){
           
            if(l1 == NULL && l2 == NULL){
                //carry not zero
                 if(carry != 0){
                    LAST->next = new ListNode(carry);
                }
                break;
            }
            else if(l1 == NULL || l2 == NULL){
                ListNode * temp2 = l1;
                if(l1 == NULL){
                    temp2 = l2;
                }
                ListNode* last;
                while(temp2 != NULL){
                    int new_val = temp2->val + carry;
                    carry = new_val/10;
                    temp2->val = new_val%10;
                    if(temp2->next == NULL){
                        last = temp2;
                    }
                    temp2 = temp2->next;
                }
                if(l1 == NULL){
                    temp->next = l2;
                }else if(l2 == NULL){
                    temp->next = l1;
                }
                if(carry != 0){
                    last->next = new ListNode(carry);
                }
                break;
                
            }
            int sum = l1->val + l2->val + carry;
            carry = sum/10;
            int new_val = sum%10;
            temp->next = new ListNode(new_val);
            temp = temp->next;
             if(l1->next == NULL || l2->next == NULL){
                LAST = temp;
            }
            l1 = l1->next;
            l2 = l2->next;
        }
        return Head->next;
    }
};


// Runtime: 20 ms, faster than 87.99% of C++ online submissions for Add Two Numbers.
// Memory Usage: 10.4 MB, less than 71.43% of C++ online submissions for Add Two Numbers.
