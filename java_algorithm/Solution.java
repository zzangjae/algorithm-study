import java.util.*;

public class Solution{
  private static int getMonthDay(int month){
    switch (month){
      case 1: return 31;
      case 3: return 31;
      case 5: return 31; 
      case 7: return 31;
      case 10: return 31;
      case 12: return 31;
      case 2: return 28;
      case 4: return 30;
      case 6: return 30; 
      case 9: return 30;
      case 11: return 30;
      default: return 0;
    }
  }


  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    sc.nextLine();

    for (int test_case = 1; test_case <= T; test_case++){
      List<String> str_num_lst = new ArrayList<>();
      str_num_lst = Arrays.asList(sc.nextLine().split(""));
      String strYear =String.join("",str_num_lst.subList(0, 4));
      String strMonth =String.join("",str_num_lst.subList(4, 6));
      String strDay =String.join("",str_num_lst.subList(6, 8));
      
      int year = Integer.parseInt(String.join("",str_num_lst.subList(0, 4)));
      int month = Integer.parseInt(String.join("",str_num_lst.subList(4, 6)));
      int day = Integer.parseInt(String.join("",str_num_lst.subList(6, 8)));
      
      if (1 <= month && month <= 12 && 1 <= day && day <= getMonthDay(month)){
        System.out.println(String.format("#%d %s/%s/%s",test_case, strYear, strMonth, strDay));
      } else{
        System.out.println(String.format("#%d -1", test_case));
      }
    }
  }
}