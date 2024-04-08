
/**Optimal Solution - Tabulation/Bottom Up Approach
 * @Time Complexity : O(n)
 * @Space Complexity: O(1)
 * @param {[number]}-> nums 
 * @returns {number} -> max amount of money that can be robbed
 */
function houseRobber (nums) {
    let rob1 = 0
    let rob2 = 0

    for (let i =0; i < nums.length; i++) {
        let temp = Math.max(rob1 + nums[i], rob2)
        rob1 = rob2
        rob2 = temp
    } 
    return rob2
}


/**Solution2 -> Memoization/Top Down Approach
 * @Time Complexity : O(n)
 * @Space Complexity: O(n)
 * @param {[number]} nums 
 * @returns {number} -> max amount of money that can be robbed
 */
function houseRobber(nums, memo=[]) {
    if (nums.length < 2) {
        return nums[0]
    }
    memo[0] = nums[0]
    memo[1] = Math.max(nums[0], nums[1])

    for (let i =2; i < nums.length; i++) {
        memo[i] = Math.max(memo[i-1], memo[i-2] + nums[i])
    }
    return memo[nums.length - 1]
}