var heightChecker = function(heights) {
    var indices = 0
    var sorted = heights.slice(0).sort()
    console.log(sorted)
    for(var i=0; i<heights.length; i++){
        if( sorted[i] != heights[i]){
          indices +=1
        }
    }
    return indices
};
heightChecker([1,1,4,2,1,3])