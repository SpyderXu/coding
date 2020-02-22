class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int N = nums.size();
        deque<int> dq;
        vector<int> res;
        for(int i = 0; i < N; i++){
            if(dq.empty()){
                dq.push_back(i);
            }
            else{
                int front_index = dq.front();
                if(i - front_index  >= k){
                    dq.pop_front();
                }
                while(!dq.empty() && nums[dq.back()] <= nums[i]){
                    dq.pop_back();
                }
                dq.push_back(i);
            }
            if(i >= k-1){
                res.push_back(nums[dq.front()]);
            }
        }
        return res;
    }
};