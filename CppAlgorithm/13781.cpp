#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;
const int SIZE = 50;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    freopen("input.txt", "r", stdin);
    int t;
    cin >> t;


    for (int tc_num = 1; tc_num <= t; tc_num++){
        int v, e;
        cin >> v >> e;

        deque<int> edges[SIZE];
        deque<int> result;

        for (int i = 0; i < e; i++){
            int s, e;
            cin >> s >> e;
            edges[s].push_back(e);
            edges[e].push_back(s);  
        }

        deque<int> node_queue(1, 1);
        bool visited[SIZE] = {false};

        while (!node_queue.empty()){
            
            int start_node = node_queue.back();
            if (!visited[start_node]) result.push_back(start_node);
            node_queue.pop_back();            

            visited[start_node] = true;

            sort(edges[start_node].begin(), edges[start_node].end(), greater<>());

            for (int node : edges[start_node]){
                if (!visited[node]) {
                    node_queue.push_back(node);
                }
            }
        }

        cout << '#' << tc_num << ' ';
        for (int num: result) cout << num << ' ';
        cout << endl;
    }

    return 0;
}