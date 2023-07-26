import java.io.BufferedInputStream;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.*;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {


    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int sangenCardConut = Integer.parseInt(bf.readLine());
        Map<Integer, Integer> sangenCards = new HashMap<>();

        for (String card: bf.readLine().split(" ")){
            if (sangenCards.containsKey(Integer.valueOf(card))){
                sangenCards.put(Integer.valueOf(card), sangenCards.get(Integer.valueOf(card))+1);
            }
            else{
                sangenCards.put(Integer.valueOf(card), 1);
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int numConut = Integer.parseInt(bf.readLine());

        for (String num: bf.readLine().split(" ")){
            if (sangenCards.containsKey(Integer.valueOf(num))){
                bw.write(sangenCards.get(Integer.valueOf(num)).toString());
                bw.write(" ");
            }
            else{
                bw.write("0 ");
            }
        }

        bw.flush();
        bw.close();
    }
}
