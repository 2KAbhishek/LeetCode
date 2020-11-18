/**
 ** Definition for singly-linked list.
 ** struct ListNode {
 **     int val;
 **     ListNode *next;
 **     ListNode() : val(0), next(nullptr) {}
 **     ListNode(int x) : val(x), next(nullptr) {}
 **     ListNode(int x, ListNode *next) : val(x), next(next) {}
 ** };
 **/
class Solution {
    public:
        int getDecimalValue(ListNode* head) {
            /* string num = to_string(head->val); */
            int num = head->val;
            while (head->next) {
                /* num += to_string(head->next->val); */
                /* num = num * 2 + head->next->val; */
                num = num << 1 | head->next->val;
                head = head->next;
            }
            /* return stoi(num,0,2); */
            return num;
        }
}