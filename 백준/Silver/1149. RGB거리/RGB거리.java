import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int n;
	static int[][] costLst;
	static int[][] resultLst;
	
	static void getMin(int tempSum, int depth, int bIdx) {
		
		if (depth == n) {
			return;
		}
		
		for (int i=0; i<3; i++) {
			if (i != bIdx) {
				if (resultLst[depth][i] == 0 || tempSum + costLst[depth][i] < resultLst[depth][i]) {
					resultLst[depth][i] = tempSum + costLst[depth][i];
					getMin(tempSum + costLst[depth][i], depth+1, i);
				}
			}
		}
	}
	
	
	public static void main(String[] args) throws IOException  {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		costLst = new int[n][3];
		resultLst = new int[n][3];
		
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<3; j++) {
				costLst[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		getMin(0, 0, -1);
		
		int result = 100*1000;
		for (int i: resultLst[n-1]) {
			if(i<result) {
				result = i;
			}
		}
		System.out.println(result);
	}
}
