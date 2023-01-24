import java.util.Stack;

public class queue_stack
{
    public static void main(String [] args) throws Exception
    {
        queue_stack p = new queue_stack();

        p.enqueue(1);
        System.out.println(p.dequeue());

        p.enqueue(1);
        p.enqueue(2);
        System.out.println(p.dequeue());
        p.enqueue(3);
        System.out.println(p.dequeue());
        System.out.println(p.dequeue());

        try 
        {
            System.out.println(p.dequeue());
        } 
        catch (Exception e) 
        {
            System.out.println(e);
        }
    }

    Stack<Integer> inqueue = new Stack<Integer>();
    Stack<Integer> outqueue = new Stack<Integer>();

    void enqueue(int number)
    {
        inqueue.push(number);
    }

    int dequeue() throws Exception
    {
        if (outqueue.size() > 0)
            return outqueue.pop();

        if (inqueue.size() > 0)
        {
            int in_size = inqueue.size();
            for (int idx = 0; idx < in_size; idx++)
                outqueue.push(inqueue.pop());

            return outqueue.pop();
        }

        throw new Exception("No more to dequeue");
    }
}