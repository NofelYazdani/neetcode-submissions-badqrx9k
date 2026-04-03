class KthLargest {
    List<Integer> arr;
    int k_number;

    public KthLargest(int k, int[] nums) {
        k_number = k;
        arr = new ArrayList();
        for (int i = 0; i < nums.length; i++){
            arr.add(nums[i]);
        }
    }
    
    public int add(int val) {
        arr.add(val);
        Collections.sort(arr);
        return arr.get(arr.size() - k_number);
        
    }
}
