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
    ListNode* mergeList(ListNode* head1, ListNode* head2){
        if(head1 == NULL){
            return head2;
        }
        else if(head2 == NULL){
            return head1;
        }
        else{
            ListNode* new_head = new ListNode(0);
            ListNode*p = new_head;
            ListNode* p1 = head1;
            ListNode* p2 = head2;
            while(p1 != NULL && p2 != NULL){
                if(p1->val < p2->val){
                    p->next = p1;
                    p1 = p1->next;
                }
                else{
                    p->next = p2;
                    p2 = p2->next;
                }
                p = p->next;
            }
            if(p1 != NULL){
                p->next = p1;
            }
            if(p2 != NULL){
                p->next = p2;
            }
            ListNode* res = new_head->next;
            delete new_head;
            return res;
        }
    }
    void seperateList(ListNode* head, ListNode** p1, ListNode** p2){
        if(head == NULL || head->next == NULL){
            *p1 = head;
            *p2 = NULL;
        }
        else{
            ListNode* pslow = head;
            ListNode* pfast = head;
            ListNode* prev = pslow;
            while(pfast != NULL && pfast->next != NULL){
                prev = pslow;
                pslow = pslow->next;
                pfast = pfast->next->next;
            }
            prev->next = NULL;
            *p1 = head;
            *p2 = pslow;
        }

    }
    ListNode* sortList(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return head;
        }
        ListNode *p1 = NULL;
        ListNode *p2 = NULL;
        seperateList(head, &p1, &p2);
        p1 = sortList(p1);
        p2 = sortList(p2);
        return mergeList(p1, p2);
    }
};