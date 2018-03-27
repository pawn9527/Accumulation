# encoding: utf-8
class ListNode:
    '''
    链表相关算法
    链表的节点
    '''

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def __init__(self):
        self.head = None

    def findKth_to_tail(self, head, k):
        '''
        问题: 输入一个链表，输出该链表中倒数第k个结点。
        '''
        node_list = []
        while head is not None:
            node_list.append(head)
            head = head.next
        if k > len(node_list) or k < 1:
            return None
        return node_list[-k]

    def reverse_list(self, pHead):
        """
        输入一个链表，反转链表后，输出链表的所有元素。
        :param p_head:
        :return:
        """
        if not pHead:
            return None
        pre = None
        while pHead:
            next_node = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = next_node
        return pre

    def Merge(self, p_head1, p_head2):
        """
        输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
        """
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2

    def HasSubtree(self, pRoot1, pRoot2):
        """
        输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
        """
        left = pRoot1.left
        right = pRoot1.right
        if left and left.val == pRoot2.val:
            self.HasSubtree(left, pRoot2.left)
            return True
        else:
            return False
        if right and right.val == pRoot2.val:
            self.HasSubtree(right, pRoot2.right)
            return True
        else:
            return False

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3

    solution = Solution()
    # print(solution.FindKthToTail(node1, 1))
    print(solution.reverse_list(node1))
