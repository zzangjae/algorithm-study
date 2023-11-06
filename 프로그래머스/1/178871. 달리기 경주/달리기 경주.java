import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> playerIdx = new HashMap<>();
        
        for (int idx = 0; idx < players.length; idx++) {
            playerIdx.put(players[idx], idx);
        }
        
        for (String calling: callings) {
            int idx = playerIdx.get(calling);
            String tempPlayer = players[idx-1];
            
            playerIdx.put(calling, idx-1);
            players[idx-1] = calling;
            
            playerIdx.put(tempPlayer, idx);
            players[idx] = tempPlayer;
        }
        
        return players;
    }
}