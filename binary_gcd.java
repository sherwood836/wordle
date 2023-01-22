import java.util.ArrayList;

public class binary_gcd
{
    static class Node
    {
        public int value;
        Node left, right;
    
        public Node(int value)
        {
            this.value = value;
        }
    }

    static class Tuple<T>
    {
        public T t1, t2;

        public Tuple(T t1, T t2)
        {
            this.t1 = t1;
            this.t2 = t2;
        }

        public String toString()
        {
            return "" + t1 + ", " + t2;
        }
    }


    public static void main(String [] args)
    {
        binary_gcd p = new binary_gcd();

        System.out.println(p.gcd(4, 8));
        System.out.println(4);
        System.out.println(p.gcd(8, 4));
        System.out.println(4);

        Node node6 = new Node(6);
        Node node9 = new Node(9);
        Node node8 = new Node(8);
        Node node4 = new Node(4);
        Node node5 = new Node(12);
        Node node3 = new Node(6);
        Node node1 = new Node(1);
        node3.left = node6;
        node3.right = node9;
        node5.left = node4;
        node5.right = node8;
        node1.left = node3;
        node1.right = node5;

        System.out.println(p.maxGCD(node1));
        System.out.println(new Tuple<Integer>(new Integer(6), new Integer(1)));

        node6 = new Node(6);
        node9 = new Node(9);
        node8 = new Node(8);
        node4 = new Node(4);
        node5 = new Node(5);
        node3 = new Node(3);
        node1 = new Node(1);
        node3.left = node6;
        node3.right = node9;
        node5.left = node4;
        node5.right = node8;
        node1.left = node3;
        node1.right = node5;

        System.out.println(p.maxGCD(node1));
        System.out.println(new Tuple<Integer>(new Integer(4), 5));

        ArrayList<Integer> big_list = new ArrayList<Integer>();
        for (Integer i = 1; i <= 32; i++)
            big_list.add(i * (i+1));
        Node node32 = p.make_node(big_list, 0);
        System.out.println(p.maxGCD(node32));
        System.out.println(new Tuple<Integer>(62, 240));

        big_list = new ArrayList<Integer>();
        for (Integer i = 1; i <= 64; i++)
            big_list.add(i * (i+1));
        node32 = p.make_node(big_list, 0);
        System.out.println(p.maxGCD(node32));
        System.out.println(new Tuple<Integer>(126, 992));

    }

    Node make_node(ArrayList<Integer> arr, int indx)
    {
        Node node = new Node(arr.get(indx));

        if (indx * 2 + 1 < arr.size() && arr.get(indx * 2 + 1) != -1)
            node.left = make_node(arr, indx * 2 + 1);
        if (indx * 2 + 2 < arr.size() && arr.get(indx * 2 + 2) != -1)
            node.right = make_node(arr, indx * 2 + 2);

        return node;
    }

    int gcd(int int1, int int2)
    {
        if (int2 == 0) return int1;

        return gcd(int2, int1%int2);
    }

    Tuple<Integer> maxGCD(Node node)
    {
        return find_gcd_and_node(node); 
    }

    Tuple<Integer> find_gcd_and_node(Node node)
    {
        Integer max_gcd = null;
        Integer max_node_value = null;

        if (node.left != null && node.right != null)
        {
            Tuple<Integer> right_value = null, left_value = null;

            if (node.left != null)
            {
                left_value = find_gcd_and_node(node.left);
            }
            if (node.right != null)
            {
                right_value = find_gcd_and_node(node.right);
            }
        
            max_gcd = gcd(node.left.value, node.right.value);
            max_node_value = node.value;

            if (right_value != null)
            {
                if (right_value.t1 > max_gcd)
                {
                   max_gcd = right_value.t1;
                   max_node_value = right_value.t2; 
                }
            }

            if (left_value != null)
            {
                if (left_value.t1 > max_gcd)
                {
                   max_gcd = left_value.t1;
                   max_node_value = left_value.t2; 
                }
            }

        }

        if (max_gcd != null)
        {
            return new Tuple<Integer>(max_gcd, max_node_value);
        }

        return null;
    }
}