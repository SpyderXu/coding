void exchange_element(vector<int>& nums, int i, int j){
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
}
int partition(vector<int>& nums, int l, int r){
    int key_val = nums[l];
    int i = l + 1;
    int j = r;
    while(i < j){
        while(i < r && nums[i] <= key_val){i++;}
        while(j > l && nums[j] > key_val){j--;}
        if(i >= j){break;}
        exchange_element(nums, i, j);
    }
    exchange_element(nums, j, l);
    return j;
}
int quick_sort(vector<int>& nums, int l, int r, int K){
    if(l >= r){
        return -1;
    }
    int part_pos = partition(nums, l, r, K);
    if(part_pos == K){
        return nums[K];
    }
    else if(part_pos > K){
        return quick_sort(nums, l, part_pos-1, K);
    }
    else{
        return quick_sort(nums, part_pos+1, r, K);
    }
}
