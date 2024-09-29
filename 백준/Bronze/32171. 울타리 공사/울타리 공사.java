import java.util.*;
import java.io.*;

/**
 * 아이디어
 * 울타리 범위를 넘어가는 직사각형 건물이 지어질 때마다 울타리를 새로 지어야 한다.
 * 울타리 범위를 넘어 가는 것은 울타리 직사각형의 변들을 조건으로 하여 체크하면 되겠다.
 *
 * 구현
 * 1. 건물의 수 N을 입력 받는다. 이후 N번에 거쳐 지어질 건물들의 좌표값들을 입력 받는다.
 * 2. 건물들의 좌표값을 입력 받을 때 다음과 같은 절차를 거친다.
 *  - 첫번째 건물일 경우 첫 건물에 맞추어 울타리를 짓는다.
 *  - 두번째 이후 부터는 울타리 범위를 넘어가는 경우 울타리를 새로 짓고 그 외에는 울타리를 짓지 않는다.
 *  - 울타리를 새로 짓는 경우 추가되는 비용을 더하여 비용을 추가하여 출력한다.
 *
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 건물의 수 N을 입력 받고 N번에 거쳐 지어질 건물들의 좌표 값을 입력 받는다.
        int n = Integer.parseInt(br.readLine());

        // 첫번 째 건물의 경우 첫 건물에 맞춰 울타리를 건설한다.
        st = new StringTokenizer(br.readLine());
        int fenceMinX = Integer.parseInt(st.nextToken());
        int fenceMinY = Integer.parseInt(st.nextToken());
        int fenceMaxX = Integer.parseInt(st.nextToken());
        int fenceMaxY = Integer.parseInt(st.nextToken());

        int cost = 2 * (fenceMaxX - fenceMinX) + 2 * (fenceMaxY - fenceMinY);
        System.out.println(cost);

        // 두번 째 이후 부터는 울타리 범위를 넘어가는 건물일 경우 울타리를 새로 짓고 그 외에는 짓지 않는다. (새로 짓는 경우 비용을 추가)
        for (int i=0; i<n-1; i++) {
            st = new StringTokenizer(br.readLine());
            int buildingMinX = Integer.parseInt(st.nextToken());
            int buildingMinY = Integer.parseInt(st.nextToken());
            int buildingMaxX = Integer.parseInt(st.nextToken());
            int buildingMaxY = Integer.parseInt(st.nextToken());

            if (buildingMinX < fenceMinX) fenceMinX = buildingMinX;
            if (buildingMinY < fenceMinY) fenceMinY = buildingMinY;
            if (buildingMaxX > fenceMaxX) fenceMaxX = buildingMaxX;
            if (buildingMaxY > fenceMaxY) fenceMaxY = buildingMaxY;

            cost = 2 * (fenceMaxX - fenceMinX) + 2 * (fenceMaxY - fenceMinY);
            System.out.println(cost);
        }
    }
}
