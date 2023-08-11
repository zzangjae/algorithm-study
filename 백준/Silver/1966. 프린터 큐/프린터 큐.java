import java.util.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        
        int tcCount = sc.nextInt();
        
        for (int i=0; i<tcCount; i++) {
        	int n = sc.nextInt();
        	int m = sc.nextInt();
        	
        	ArrayDeque<Integer> arrayDeque = new ArrayDeque<Integer>();
        	PriorityQueue<Integer> priorityQueue = new PriorityQueue<Integer>((o1, o2) -> o2 - o1);
        	
        	for (int j=0; j<n; j++) {
        		int num = sc.nextInt();
        		arrayDeque.add(num);
        		priorityQueue.add(num);
        	}
        	
        	while(m >= 0) {
        		int num = arrayDeque.poll();
        		
        		if (num == priorityQueue.peek()){
        			m--;
        			priorityQueue.poll();
        			continue;
        		}
        		else {
        			m = (m > 0) ? m - 1 : arrayDeque.size();
        			arrayDeque.add(num);      			
        		}
        	}
        	
        	System.out.println(n - arrayDeque.size());
        }
    }
}
