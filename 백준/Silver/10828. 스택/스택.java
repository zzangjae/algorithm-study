import java.io.BufferedInputStream;
import java.util.*;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        Stack<Integer> stack = new Stack<>();

        for (int i=0; i <n; i++){
            String[] commands = bf.readLine().split(" ");

            if (commands[0].equals("push")){
                stack.add(Integer.parseInt(commands[1]));
            }
            else if (commands[0].equals("pop")) {
                System.out.println(stack.isEmpty() ? -1: stack.pop());
            }
            else if (commands[0].equals("size")){
                System.out.println(stack.size());
            }
            else if (commands[0].equals("empty")){
                System.out.println(stack.isEmpty() ? 1: 0);
            }
            else if (commands[0].equals("top")){
                System.out.println(stack.isEmpty() ? -1 : stack.lastElement() );
            }
        }
    }
}
