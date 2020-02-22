class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int N = nums.size();
        int K = N/2;
        int l = 0;
        int r = K;
        while(l < r){
            int mid = (l + r)/2;
            if(nums[2*mid] == nums[2*mid + 1]){
                l = mid + 1;
            }
            else{
                r = mid;
            }
        }
        return nums[2*l];
    }
};