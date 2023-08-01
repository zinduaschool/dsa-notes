
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