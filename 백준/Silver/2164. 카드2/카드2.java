import java.util.*;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws FileNotFoundException{
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		LinkedList<Integer> cards = new LinkedList<>();
		
		for (int i=1; i<=n; i++) {
			cards.add(i);
		}
		
		while (cards.size() > 1) {
			cards.removeFirst();
			cards.addLast(cards.getFirst());
			cards.removeFirst();
		}
		
		System.out.println(cards.getFirst());
	}
}
