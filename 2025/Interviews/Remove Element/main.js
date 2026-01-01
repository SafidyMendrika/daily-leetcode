
(function main(){
    let nums = [3, 2, 2, 3];
    let val = 3;
    console.log(nums);
    
    let result = removeElement(nums, val);
    console.log(result);
    console.log(nums);
})()

function removeElement(nums, val) {
    let k = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}