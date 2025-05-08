/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  let res = nums[0];
  let total = 0;

  for (let n of nums) {
      if (total < 0) {
          total = 0;
      }

      total += n;
      res = Math.max(res, total);
  }
  
  return res;    
};