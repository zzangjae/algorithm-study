import java.util.*;

public class Solution{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();

    for (int test_case = 1; test_case <= T; test_case ++){
      int left_num = sc.nextInt();
      int right_num = sc.nextInt();

      if (left_num > right_num){
        System.out.println(String.format("#%d >", test_case));
      }
      else if (left_num < right_num){
        System.out.println(String.format("#%d <", test_case));
      }
      else{
        System.out.println(String.format("#%d =", test_case));
      }
    }
  }
}