import java.util.ArrayList;

public class palindrome
{
    public static void main(String [] args)
    {
        palindrome p = new palindrome();

        System.out.println(p.is_palindrome("aabbbbaa"));
        System.out.println(p.is_palindrome("aabbBbaa"));
        System.out.println(p.is_palindrome("aabbbaa"));

        System.out.println(p.all_palindrome("aabbbbaa"));
        System.out.println(p.all_palindrome("aabbBbaa"));
        System.out.println(p.all_palindrome("aabbbaa"));
    }

    boolean is_palindrome(String str)
    {
        int mid = (int)(str.length() / 2);
        String rev_str = new String();

        for (String x:str.substring(0, mid).split(""))
        {
            rev_str = x.concat(rev_str);
        }

        return rev_str.equals(str.substring((int)((str.length() + 1) / 2), str.length()));
    }

    ArrayList<String> all_palindrome(String str)
    {
        ArrayList<String> all_list = new ArrayList<String>();

        for (int beg_idx = 0; beg_idx <= str.length(); beg_idx++)
        {
            for (int end_idx = beg_idx + 2; end_idx <= str.length(); end_idx++)
            {
                if (is_palindrome(str.substring(beg_idx, end_idx)))
                {
                    all_list.add(str.substring(beg_idx, end_idx));
                }
            }
        }


        return all_list;
    }

}