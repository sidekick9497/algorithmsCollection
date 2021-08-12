var removeDuplicates = function(nums) {
    var len = nums.length
    if(len == 0 ){
        return 0
    }
    var fillIndex = 1
    var i  = 1 //start from the second index
    while(i < len) {
        if(nums[i]!=nums[fillIndex-1]){
            nums[fillIndex] = nums[i]  //compare with previous value and copy if its different
            fillIndex++
        }
        i++
       
}
    return fillIndex
};
console.log(removeDuplicates([1,1]))