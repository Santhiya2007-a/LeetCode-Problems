class Solution:
    def addTwoNumbers(self, list1, list2):
        l1 = []
        l2 = []
        while list1:
            l1.append(list1.val)
            list1 = list1.next

        while list2:
            l2.append(list2.val)
            list2 = list2.next

        result = []
        carry = 0

        n = max(len(l1), len(l2))

        for i in range(n):
            x = l1[i] if i < len(l1) else 0
            y = l2[i] if i < len(l2) else 0

            total = x + y + carry
            result.append(total % 10)
            carry = total // 10

        if carry:
            result.append(carry)
        dummy = ListNode(0)
        current = dummy

        for num in result:
            current.next = ListNode(num)
            current = current.next

        return dummy.next