class ListNode:
  def __init__(self, val:int =0 , next:ListNode = None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumber(self, l1:Optional[ListNode],l2: Optional[ListNode]):
    carryover:int =0 
    dummy = ListNode(0)
    curr = dummy
    p,q = l1,l2
    while p is not None or q is not None or carryover:
      x= p.val if p is not None else 0
      y = q.val if q is not None else 0
      target = x+y+carryover
      curr.next = ListNode(target%10)
      carryover = target//10
      curr = curr.next 
      if p is not None:
        p= p.next 
      if q is not None:
        q = q.next 
   return dummy.next
