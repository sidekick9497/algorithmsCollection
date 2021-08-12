var removeElement = function(nums, val) {
    
    var pointer = nums.length - 1
    var index = 0
    while(index < pointer) {
        if(nums[index] == val) {
            if(nums[pointer] == val){
                while(nums[pointer] ==val){
                    nums[pointer] = "-"
                    pointer--
                }
            }
            
            nums[index] = nums[pointer]
            nums[pointer] = "-"
            pointer--
        }
        index++
    }
    return nums
};
nums = [0,1,2,2,3,0,4,2]
val = 2

console.log(removeElement(nums,val))