import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        
        int n = photo.length;
        int[] answer = new int[n];
        
        Map<String, Integer> map = new HashMap<>();
        
        for (int i=0; i<name.length; i++) {
            map.put(name[i], yearning[i]);
        }
        
        for (int i=0; i<n; i++) {
            int sum = 0;
            
            for (String str: photo[i]) {
                if (map.containsKey(str)) sum += map.get(str);
            }        
            
            answer[i] = sum;
        }
        
        return answer;
    }
}