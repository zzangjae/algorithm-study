import java.util.*;

public class Solution{
  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    String alphabets = sc.nextLine();

    for (int i = 0; i < alphabets.length(); i++){
      Character tempChar = alphabets.charAt(i);
      System.out.print(((int) tempChar - (int) 'a') + 1);
      System.out.print(" ");
    }

  }
}