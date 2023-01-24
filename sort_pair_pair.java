import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class sort_pair_pair
{
    static class Pair implements Comparable
    {
        public int a, b;
    
        public Pair(int a, int b)
        {
            this.a = a;
            this.b = b;
        }

        public int compareTo(Object o)
        {
            Pair p2 = (Pair)o;
            return new Integer(this.a).compareTo(new Integer(p2.a));
        }
    }

    public static void main(String [] args)
    {
        sort_pair_pair p = new sort_pair_pair();

        Pair pair6 = new Pair(10, 30);
        Pair pair9 = new Pair(50, 65);
        Pair pair8 = new Pair(65, 80);
        Pair pair4 = new Pair(85, 100);
        Pair pair5 = new Pair(35, 55);
        Pair pair3 = new Pair(35, 85);
        Pair pair1 = new Pair(15, 20);
        Pair pair10 = new Pair(25, 26);
        Pair pair11 = new Pair(26, 30);
        Pair pair12 = new Pair(27, 30);

        // self.assertEqual(find_chain([]), 0)
        ArrayList<Pair> big_list = new ArrayList<Pair>();
        System.out.println(p.find_chain(big_list));
        System.out.println(0);

        // self.assertEqual(find_chain([[10, 30]]), 1)
        big_list = new ArrayList<Pair>(Arrays.asList(pair6));
        System.out.println(p.find_chain(big_list));
        System.out.println(1);

        // self.assertEqual(find_chain([[10, 30], [50, 65], [65, 80]]), 2)
        big_list = new ArrayList<Pair>(Arrays.asList(pair6, pair9, pair8));
        System.out.println(p.find_chain(big_list));
        System.out.println(2);

        // self.assertEqual(find_chain([[10, 30], [85, 100], [65, 80]]), 3)
        big_list = new ArrayList<Pair>(Arrays.asList(pair6, pair9, pair4));
        System.out.println(p.find_chain(big_list));
        System.out.println(3);

        // self.assertEqual(find_chain([[10, 30], [85, 100], [65, 80], [35, 55]]), 4)
        big_list = new ArrayList<Pair>(Arrays.asList(pair6, pair4, pair8, pair5));
        System.out.println(p.find_chain(big_list));
        System.out.println(4);

        // self.assertEqual(find_chain([[10, 30], [85, 100], [65, 80], [35, 85]]), 3)
        big_list = new ArrayList<Pair>(Arrays.asList(pair6, pair4, pair8, pair3));
        System.out.println(p.find_chain(big_list));
        System.out.println(3);

        // self.assertEqual(find_chain([[10, 30], [15, 20]]), 1)
        big_list = new ArrayList<Pair>(Arrays.asList(pair6, pair1));
        System.out.println(p.find_chain(big_list));
        System.out.println(1);

        // self.assertEqual(find_chain([[5, 24], [39, 60], [15, 28], [27, 40], [50, 90] ]), 3)
        big_list = new ArrayList<Pair>(Arrays.asList(new Pair(5, 24), new Pair(39, 60), new Pair(15, 28), new Pair(27, 40), new Pair(50, 90)));
        System.out.println(p.find_chain(big_list));
        System.out.println(3);

        // self.assertEqual(find_chain([[10, 30], [25, 26], [26, 30], [35, 85]]), 2)
        big_list = new ArrayList<Pair>(Arrays.asList(pair6, pair10, pair11, pair3));
        System.out.println(p.find_chain(big_list));
        System.out.println(2);

        // self.assertEqual(find_chain([[10, 30], [25, 26], [27, 30], [35, 85]]), 3)
        big_list = new ArrayList<Pair>(Arrays.asList(pair6, pair10, pair12, pair3));
        System.out.println(p.find_chain(big_list));
        System.out.println(3);
    }

    int find_chain(ArrayList<Pair> arr)
    {
        Collections.sort(arr); 
        ArrayList<Pair> final_list = new ArrayList<Pair>();

        if (arr.size() > 0)
        {
            final_list.add(arr.get(0));

            if (arr.size() > 1)
            {
                for (int idx = 1; idx < arr.size(); idx++)
                {
                    if (final_list.get(final_list.size() -1).b < arr.get(idx).a)
                        final_list.add(arr.get(idx));
                    else if (final_list.get(final_list.size() -1).b > arr.get(idx).b)
                    {
                        final_list.remove(final_list.size() -1);
                        final_list.add(arr.get(idx));
                    }
                }
            }
        }

        return final_list.size();
    }
}