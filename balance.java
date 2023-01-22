
public class balance
{
    public static void main(String [] args)
    {
        balance p = new balance();

        System.out.println(p.balance_than(""));
        System.out.println(p.balance_than("<"));
        System.out.println(p.balance_than(">"));
        System.out.println(p.balance_than("><<><>><>>"));
        System.out.println(p.balance_than("><<<<<><>><>>"));
        System.out.println(p.balance_than("<<>>>>>>>"));
        System.out.println(p.balance_than("<<<<<<><>"));
        System.out.println(p.balance_than(">><<<<<<><>"));
        System.out.println(p.balance_than("><>><<<<<<><>"));

    }

    String balance_than(String str)
    {
        if ("".equals(str)) return "";

        int less_than_num = 0;
        int more_to_beginning = 0;

        for (String x:str.split(""))
        {
            if ("<".equals(x))
            {
                less_than_num++; 
            }
            else if (">".equals(x))
            {
                less_than_num--;

                if (less_than_num <= 0)
                {
                    // We need to add more to the beginning
                    more_to_beginning++;                    
                }
            }
        }

        if (more_to_beginning > 0)
        {
            for (int i = 0; i < more_to_beginning; i++)
            {
                str = "<" + str;
                less_than_num++;
            }
        }

        if (less_than_num > 0)
        {
            for (int i = 0; i < less_than_num; i++)
            {
                str = str + ">";
            }
        }
        else
        {
            for (int i = 0; i < -less_than_num; i++)
            {
                str = "<" + str;
            }

        }

        return str;
    }

}