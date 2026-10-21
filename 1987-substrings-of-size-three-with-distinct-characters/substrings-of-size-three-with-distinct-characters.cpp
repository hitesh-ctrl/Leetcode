#include <set>
using namespace std;
class Solution {
public:
    int countGoodSubstrings(string s) {
        
        int n = s.size();
        int count = 0;
        for (int i = 0; i<=n-3;i++){
            set<char> st = {s[i], s[i+1], s[i+2]};
            if(st.size() == 3){
                count++;
            }


        }
        return count;
    }
};