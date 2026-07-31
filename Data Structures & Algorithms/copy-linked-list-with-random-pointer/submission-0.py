"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        OldToCopy={None:None}
        cur=head    
        while cur:
            OldToCopy[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            copy=OldToCopy[cur]
            copy.next=OldToCopy[cur.next]
            copy.random=OldToCopy[cur.random]
            cur=cur.next
        return OldToCopy[head]