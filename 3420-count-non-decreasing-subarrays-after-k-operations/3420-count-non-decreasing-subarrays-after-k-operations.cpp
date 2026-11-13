#define ll long long
class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        ll n = nums.size();
        ll right = n - 1;
        ll operation = 0;
        ll result = 0;
        deque<pair<ll, ll>> d;
        for (ll left = n - 1; left >= 0; left--) {
            ll c = 1;
            while (!d.empty() && nums[left] > d.front().first) {
                auto [num, cnt] = d.front();
                d.pop_front();
                operation += (nums[left] - num) * cnt;
                c += cnt;
            }
            d.push_front({nums[left], c});

            while (operation > k) {
                auto [num, cnt] = d.back();
                operation -= num - nums[right--];
                cnt--;
                d.back().second--;
                if (cnt == 0) {
                    d.pop_back();
                }
            }

            result += right - left + 1;
        }

        return result;
    }
};