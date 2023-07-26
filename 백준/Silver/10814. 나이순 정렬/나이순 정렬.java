import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args){
        Scanner sc = new Scanner(new InputStreamReader(System.in));

        int n = Integer.parseInt(sc.nextLine());
        Map<String, Queue<String>> userMap = new HashMap<>();

        for(int i=0; i<n; i++){
            String userInfo = sc.nextLine();
            String key = userInfo.split(" ")[0];

            if (userMap.containsKey(key)){
                userMap.get(key).add(userInfo);
            }
            else{
                Queue<String> queue = new LinkedList<>();
                queue.add(userInfo);
                userMap.put(key, queue);
            }
        }

        for(int i=1; i<=200; i++){
            if (userMap.containsKey(String.valueOf(i))){
                for(String userInfo: userMap.get(String.valueOf(i))){
                    System.out.println(userInfo);
                }
            }
        }
    }
}