using System;

public class MinStack {
    int min = int.MaxValue;
    Node head;

    private class Node {
        public int data;
        public Node next;

        public Node(int data) {
            next = null;
            this.data = data;
        }
    }

    public MinStack() {

    }

    public void Push(int x) {
        if (x < min) {
            min = x;
        }
        Node node = new Node(min);
        node.next = new Node(x);

        if (this.head == null || head.next == null) {
            head = node;
        } else {
            Node temp = head;
            head = node;
            head.next.next = temp;
        }
    }

    public void Pop() {
        if (this.head == null) {
            // Do nothing
        } else {
            Node currHead = head.next;
            if (currHead.next != null) {
                head = currHead.next;
                min = head.data;
            } else {
                head = null;
                this.min = int.MaxValue;
            }
        }
    }

    public int Top() {
        if (head != null)
            return head.next.data;
        else
            return 0;
    }

    public int GetMin() {
        return min;

    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(x);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */
public class Solution
{
    private void calc()
    {
        MinStack minStack = new MinStack();
        int result;

        minStack.Push(-2);
        Console.WriteLine("Push(-2)");

        minStack.Push(0);
        Console.WriteLine("Push(0)");

        minStack.Push(-3);
        Console.WriteLine("Push(-3)");

        result = minStack.GetMin();
        Console.WriteLine("GetMin() --> " + result.ToString());

        minStack.Pop();
        Console.WriteLine("Pop())");

        result = minStack.Top();
        Console.WriteLine("Top()    --> " + result.ToString());

        result = minStack.GetMin();
        Console.WriteLine("GetMin() --> " + result.ToString());
    }

    public void Main()
    {
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        calc();

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
