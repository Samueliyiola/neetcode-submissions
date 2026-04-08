class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let distinct = [];
        for(const item of nums){
            for(const num of distinct){
                if(num == item){
                    return true;
                }
            }
            distinct.push(item);
        }
        return false;
    }
}
