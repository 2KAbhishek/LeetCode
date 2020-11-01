/**
 ** Definition for singly-linked list.
 ** function ListNode(val, next) {
 **     this.val = (val===undefined ? 0 : val)
 **     this.next = (next===undefined ? null : next)
 ** }
 **/
/**
 ** @param {ListNode} head
 ** @return {number}
 **/

var getDecialValue = function (head) {
    // let num = "" + head.val;
    let num = head.val;

    while (head.next) {
        // num += head.next.val;
        // num = num * 2 + head.next.val;
        num = num << 1 | head.next.val;
        head = head.next;
    }
    // return parseInt(num,2);
    return num;
}
