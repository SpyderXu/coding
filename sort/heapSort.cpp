void exchange_elements(vector<int>& nums, int i, int j){
    int tmp = nums[i];
    nums[i] =nums[j];
    nums[j] = tmp;
}
void sink(vector<int>& nums, int k, int N){
    while(2*k <= N){
        int j = 2*k;
        if(j+1 <= N && nums[j+1] < nums[j]){j++;}
        if(nums[j] < nums[k]){break;}
        exchange_element(nums, j, k);
        j = k;
    }
}
void heap_sort(vector<int>& nums){
    nums.insert(nums.begin(), 0);
    int N = nums.size()-1;
    for(int i = N/2; i >= 1; i--){
        sink(nums, i, N);
    }
    while(N > 0){
        exchange_element(nums, 1, N);
        N--;
        sink(nums, 1, N);
    }
}
int main(){
    vector<int> nums = {1,4,2,7,6,3};
    heap_sort(nums);
    for(int i = 0; i < nums.size(); i++){
        cout << nums[i] <<endl;
    }
    return 1;
}