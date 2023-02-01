import java.util.*;

public class Solution
{
  public static void main(String[] arg)
  {
    Scanner sc = new Scanner(System.in);
    int iterations = sc.nextInt();
    List<Integer> num_lst = new ArrayList<>();

    for (int iteration = 1; iteration <= iterations; iteration++){
      num_lst.add(sc.nextInt());
    }

    Collections.sort(num_lst);
    System.out.println(num_lst.get(num_lst.size()/2));
  }
}