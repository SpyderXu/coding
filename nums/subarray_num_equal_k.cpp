int subarray_num_equal_k(vector<int>& nums, int k){
    int N = nums.size();
    vector<int> pre_sum(N+1, 0);
    for(int i = 0; i < N; i++){
        pre_sum[i+1] = pre_sum[i] + nums[i];
    }
    unordered_map<int, int> dp;
    int cnt = 0;
    for(int i = 0; i < N+1; i++){
        cnt += dp[pre_sum[i]]
        dp[pre_sum[i] + k]++;
    }
    return cnt;
}