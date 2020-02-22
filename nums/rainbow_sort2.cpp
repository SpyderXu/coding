class Solution {
public:
    void swap_elem(vector<int>& nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    void sortColors(vector<int>& nums) {
        int N = nums.size();
        if(N == 0 || N == 1){
            return;
        }
        int l = 0;
        int r = N-1;
        int cur = 0;
        while(cur <= r){
            if(nums[cur] == 1){cur++;}
            else if(nums[cur] == 0){
                swap_elem(nums, cur, l);
                cur++;
                l++;
            }
            else{
                swap_elem(nums, cur, r);
                r--;
            }
        }
    }
};