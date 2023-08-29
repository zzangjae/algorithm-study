import java.util.*;
import java.io.*;

public class Main{
    static String tokens;
    static ArrayDeque<Character> stack = new ArrayDeque<>();

    public static void main(String args[]) throws FileNotFoundException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        tokens = br.readLine();

        while(!tokens.equals(".")){
            String result = "yes";

            for(Character token: tokens.toCharArray()){
                Character tempToken;
                if (token.equals('(') || token.equals('[')) stack.add(token);

                else if (token.equals(')')) {
                    if (stack.isEmpty()){
                        result = "no";
                        break;
                    }

                     tempToken = stack.pollLast();

                     if (tempToken.equals('[')) {
                         result = "no";
                         break;
                     }
                }

                else if (token.equals(']')) {
                    if (stack.isEmpty()){
                        result = "no";
                        break;
                    }

                    tempToken = stack.pollLast();

                    if (tempToken.equals('(')) {
                        result = "no";
                        break;
                    }
                }
            }

            if (!stack.isEmpty()) {
                result = "no";
            }

            stack.clear();
            System.out.println(result);
            tokens = br.readLine();
        }
    }
}
