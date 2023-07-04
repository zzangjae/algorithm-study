import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		final int m = sc.nextInt();
		final int n = sc.nextInt();
		
		int[][] tomatoBox = new int[n][m];
		LinkedList<int[]> queue = new LinkedList<>();
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++){
				tomatoBox[i][j] = sc.nextInt();
				
				if(tomatoBox[i][j] == 1) {
					int[] tempList = {i, j, 0};
					queue.add(tempList);
				}
			}
		}
		
		int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
		 
		int maxDepth = 0;
		
		while (queue.size() != 0) {
			int[] tempList = queue.getFirst();
			queue.removeFirst();
			
			for (int[] direction: directions) {
				int tn = tempList[0] + direction[0];
				int tm = tempList[1] + direction[1];
				int depth = tempList[2] + 1;
				
				if (!(0 <= tn && tn < n && 0 <= tm && tm < m)) {
					continue;
				}
				
				if (tomatoBox[tn][tm] == 0) {
					tomatoBox[tn][tm] = 1;
					int[] tList = {tn, tm, depth};
					queue.add(tList);
					
					if (maxDepth < depth) {
						maxDepth = depth;
					}
				}	
			}
		}
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if(tomatoBox[i][j] == 0) {
					maxDepth = -1;
				}
			}
		}
		
		System.out.println(maxDepth);
		
		
	}
}
