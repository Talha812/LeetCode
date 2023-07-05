class MyLinkedList {
            Node head;
    Node tail;
    public MyLinkedList() {
        head=new Node();
        tail=new Node();
        head=tail=null;
    }
    
    public int get(int index) {
        int size=size();
        if(index>=size){
            return -1;
        }
        Node temp=this.head;
        for(int i=0;i<index && temp!=null;i++){
            temp=temp.next;
        }
        return temp.val;
    }
    
    public void addAtHead(int val) {
        Node node=new Node();
        node.val=val;
        if(head==null){
            this.head=node;
            this.tail=node;
            node.next=null;
        }else{
            node.next=this.head;
            this.head=node;
        }
    }
    
    public void addAtTail(int val) {
        Node node=new Node();
        node.val=val;
        if(head==null){
            head=node;
            tail=node;
            node.next=null;
        }else{
            tail.next=node;
            node.next=null;
            tail=node;
        }
    }
    
    public void addAtIndex(int index, int val) {
        int size=size();
        Node node=new Node();
        node.val=val;
        if(index==0){
            node.next=head;
            head=node;
        }else if(index==size){
            tail.next=node;
            node.next=null;
            tail=node;
        }else if(index>size){
            return;
        }
        else{
            Node temp=head;
            for(int i=0;i<index-1;i++){
                temp=temp.next;
            }
            Node nextNode=temp.next;
            temp.next=node;
            node.next=nextNode;
        }
    }
    
    public void deleteAtIndex(int index) {
        int size=size();
        if(index==0){
            head=head.next;
        }else if(index==size-1){
            Node temp=head;
            for(int i=0;i<size-2;i++){
                temp=temp.next;
            }
            temp.next=null;
            tail=temp;
        }else if(index>=size){
            return;
        }
        else{
            Node temp=head;
            for(int i=0;i<=index-2;i++){
                temp=temp.next;
            }
            temp.next=temp.next.next;
        }
    }
    
    public int size(){
        Node temp=head;
        int count=0;
        while(temp!=null){
            count++;
            temp=temp.next;
        }
        return count;
    }
    
}

class Node{
    Node node;
    Node next;
    int val;
}


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */