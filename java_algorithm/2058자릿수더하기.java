import java.util.*;

public class Solution{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    List<String> str_num_lst = new ArrayList<>();
    str_num_lst = Arrays.asList(sc.nextLine().split(""));
    int sum = 0;

    for (String number: str_num_lst){
      sum += Integer.parseInt(number);
    }

    System.out.println(sum);
  }
}