class Solution {
public:
    string digitSum(string s, int k) {
        

        auto sum = [&](vector<string> & splitted){
            string result = "";
            for(auto s: splitted){
                int cur = 0;
                for(char c: s){
                    cur += c-'0';
                }
                result += to_string(cur);
            }
            return result;
        };

        auto splitted_sum = [&](string s){
            int n = s.size();
            vector<string> splitted;
            for(int i = 0; i<n; i+=k){
                splitted.push_back(s.substr(i, k));
            }
            return sum(splitted);
        };
        
        while(s.size() > k){
            s = splitted_sum(s);
        }
        return s;
    }
};