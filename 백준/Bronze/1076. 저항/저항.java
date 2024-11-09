import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        String[] colors = {
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"
        };
        HashMap<String, Integer> colorIdx = new HashMap<>();

        for (int i=0; i<10; i++) {
            colorIdx.put(colors[i], i);
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long result = 0;

        result += 10L * colorIdx.get(br.readLine());
        result += colorIdx.get(br.readLine());
        result *= (long) Math.pow(10, colorIdx.get(br.readLine()));

        System.out.println(result);
    }
}

