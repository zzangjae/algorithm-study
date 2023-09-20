/*
cache 를 딕셔너리로 선언하면 될 듯? key: city, value: used count

cache hit
- value 증가
- answer ++

cache miss
- LRU 실행 (cache.size >= cacheSize), cache에 추가 (cache.size < cacheSize)
- answer += 5
*/
import java.util.*;

class Solution {    
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        ArrayDeque<String> cache = new ArrayDeque<>();
        
        for (String city: cities){
            city = city.toLowerCase();
            
            if (cache.contains(city)){
                cache.addLast(city);
                cache.remove(city);
                answer++;
                continue;
            }
            
            cache.addLast(city);
            answer += 5;
            
            if (cache.size() > cacheSize){
                cache.pollFirst();
            }
        }
        
        return answer;
    }
}