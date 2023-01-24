import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class iter_of_iter implements Iterator
{
    static class MyIter implements Iterator
    {
        ArrayList arr = new ArrayList();

        public boolean hasNext()
        {
            return arr.size() > 0;
        }

        public Object next()
        {
            return arr.remove(0);
        }

    }

    public static void main(String [] args) throws Exception
    {
        iter_of_iter p = new iter_of_iter();

        MyIter list1 = new MyIter();
        MyIter list2 = new MyIter();
        MyIter list3 = new MyIter();
        list1.arr = new ArrayList(Arrays.asList(1, 2, 3));
        list2.arr = new ArrayList(Arrays.asList(4, 5));
        list3.arr = new ArrayList(Arrays.asList(6));

        p.iter_list.add(list1);
        p.iter_list.add(list2);
        p.iter_list.add(list3);

        System.out.println(p.next());
        System.out.println(p.next());
        System.out.println(p.next());
        System.out.println(p.next());
        System.out.println(p.next());
        System.out.println(p.next());
        System.out.println(p.next());

    }

    ArrayList<Iterator> iter_list = new ArrayList<Iterator>();
    int current_iter_idx = 0;

    public boolean hasNext()
    {
        if (iter_list.get(current_iter_idx).hasNext())
            return true;

        for (int idx = 1; idx <= iter_list.size(); idx++)
        {
            current_iter_idx = (current_iter_idx + idx)%iter_list.size();

            if (iter_list.get(current_iter_idx).hasNext())
                return true;
        }

        return false;
    }

    public Object next()
    {
        if (hasNext())
        { 
            Object next_value = (int)iter_list.get(current_iter_idx).next();
            current_iter_idx = (current_iter_idx + 1)%iter_list.size();
            return next_value;
        }

        return null;
    }
}