class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        
        let map = new Map<number, number>(); 

        for(let i=0; i<nums.length; i++){
            let missing = target - nums[i];
            if(map.has(missing)){
                return [map.get(missing), i]
            } else {
                map.set(nums[i], i)
            }
        }

        return null
    }
}
