class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int MOD = (int)1e9+7;
        int n = arr.size();
        vector<int> presum(n+1);
        for(int i = 0; i<n; i++){
            presum[i+1] = presum[i] + arr[i];
        }

        int even = 0, odd = 0;
        int result = 0;

        for(int i = 0; i<=n; i++){
            if(presum[i]%2){
                result = (result + even)%MOD;
                odd += 1;
            }else{
                result = (result + odd)%MOD;
                even += 1;
            }
        }
        return result%MOD;

    }
};