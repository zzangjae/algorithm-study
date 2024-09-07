import java.util.*;
import java.io.*;

/*
13458 시험 감독

1. 시험장의 개수 N, 응시자 수, B, C 를 입력 받는다.
2. 각 시험장에 대해 응시자 수 - B <= 0 이면 필요한 감독관 수 += 1
    응시자 수 - B > 0 필요한 감독관 수 += (필요한 감독관 수 - B) // C + 1 + 1
3. 필요한 감독관 수 출력
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] candidateCount = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            candidateCount[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        long result = 0;
        for (int i=0; i<n; i++) {
            if (candidateCount[i] - b <= 0) result++;
            else {
                result += (candidateCount[i] - b) / c + 1;
                result += (candidateCount[i] - b) % c != 0 ? 1 : 0;
            }
        }

        System.out.println(result);
    }
}
