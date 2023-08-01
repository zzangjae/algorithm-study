import java.util.*;
import java.io.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {

    public static int getResult(int n){

        if (n == 1){
            return 1;
        }

        if (n == 2){
            return 2;
        }

        if (n == 3){
            return 4;
        }

        return getResult(n-1) + getResult(n-2) + getResult(n-3);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());

        for (int i=0; i<n; i++){
            int num = Integer.parseInt(bf.readLine());
            System.out.println(getResult(num));
        }
    }
}
