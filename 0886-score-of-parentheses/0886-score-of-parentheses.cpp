class Solution {
public:
    int scoreOfParentheses(string s) {
        int score = 0;

        stack<int> stk;
        for(int i=0; i<s.size(); i++)
        {
            if(s[i] == '(')
            {
                stk.push(score);
                score = 0;
            }
            else
            {
                score = stk.top() + max(2*score, 1);
                stk.pop();
            }
        }

        return score;
    }
};