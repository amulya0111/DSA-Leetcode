def sortList(head):
    # write code here...
    left = temp=head
    if head is None or head.next is None:
        return head 
    zeroh=zerot=oneh=onet=twoh=twot=None
    while temp:
        # first save the upcoming separately
        nextnode=temp.next
        temp.next=None
        # check values and add accordingly 
        if temp.data==0:
            if zeroh is None:
                zeroh=zerot=temp
            else:
                zerot.next=temp
                zerot=zerot.next
        elif temp.data==1:
            if oneh is None:
                oneh=onet=temp
            else:
                onet.next=temp
                onet=onet.next
        elif temp.data==2:
            if twoh is None:
                twoh=twot=temp
            else:
                twot.next=temp
                twot=twot.next
        temp=nextnode
    # finally merge everything(handle None cases for all three, twoh sel handled)
    if zeroh:
        head=zeroh
        if oneh:
            zerot.next=oneh
            zerot=onet
        zerot.next=twoh
    elif oneh:
            head=oneh
            onet.next=twoh
    else:
        head=twoh
        
    return head
                