import java.io.*;
import java.util.*;

/**
 * 아이디어
 * 나눗셈 몫과 나머지 연산을 반복한다. 이 때 같은 구성이 나오면 순환으로 간주하자.
 *
 * 1. t를 입력 받는다.
 * 2. 각 테스트 케이스에 대해 HashMap을 이용하여 나누기 대상이 되는 숫자와 index를 기록한다.
 * 3. 순환되는 부분이 나오면 종료.
 */
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());

        for (int i=0; i<t; i++) {
            String result = "";
            Map<Integer,Integer> map = new HashMap<>();

            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            int den = Integer.parseInt(st.nextToken());

            result += num / den + ".";
            num = num % den * 10;
            int idx = 0;
            String decimal = "";

            while(!map.containsKey(num)) {
                map.put(num, idx++);
                decimal += num / den;
                num = num % den * 10;
            }

            result += decimal.substring(0, map.get(num));
            result += "(" + decimal.substring(map.get(num), idx) + ")";

            System.out.println(result);
        }
    }
}
