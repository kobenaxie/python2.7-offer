class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers) {
        int len=numbers.size(), start=0, end=numbers.size()-1;
        quick_sort(numbers, start, end, len);
        int number = numbers[len/2];
        if(count(numbers.begin(), numbers.end(), number) <=len/2)
            return 0;
        return number;
    }
    
    int partition(vector<int> arr, int start, int end, int len){
        // find a number and put it end
        int idx = end-1;
        swap_vector(arr, idx, end);
        
        int small = start-1;
        for(idx=start; idx<end; ++idx){
            if(arr[idx] < arr[end]){
                ++small;
                // small != idx means arr[idx]<arr[end] and arr[small]>arr[end]
                if(small != idx)
                    swap_vector(arr, small, idx);
            }
        }
        // put arr[end] back to middle
        ++small;
        swap_vector(arr, small, end);
        return small;
    }
    
    void quick_sort(vector<int>& arr, int start, int end, int len){
        if(start==end){
            return;
        }
        int idx = partition(arr, start, end, len);
        if (idx>start){
            quick_sort(arr, start, idx-1, len);
        }
        if (idx<end){
            quick_sort(arr, idx+1,end, len);
        }
    }
    
    void swap_vector(vector<int> arr, int i, int j){
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
};
