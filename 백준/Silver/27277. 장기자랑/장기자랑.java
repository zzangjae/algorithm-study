import java.io.*;
import java.util.*;

import static java.lang.Math.max;

/**
 * 장기자랑
 *
 * 핵심 아이디어 합을 극대화 하는 방법은
 * 실력이 가장 큰 값과 작은 값을 순서대로 번갈아가면서 놓는 것이다.
 *
 * 직관으로 풀이한 거라 수학적 증명을 해보고 싶음..
 */
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] soldierTalent = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            soldierTalent[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(soldierTalent);

        int sum = 0;
        int[] newSortedSoldier = new int[n];

        // 크고 작은 순서대로 번갈아가면서 배열
        for (int i=0; i<n; i++) {
            if (i % 2 == 0) newSortedSoldier[i] = soldierTalent[n-1-i/2];
            else newSortedSoldier[i] = soldierTalent[i/2];
        }

        for (int i=0; i<n; i++) {
            if (i>0) sum += max(0, newSortedSoldier[i] - newSortedSoldier[i-1]);
            else sum += newSortedSoldier[i];
        }

        System.out.println(sum);
    }
}
