function peakFinder(items) {
    var index = 0
    while(index < items.length) {
        if(index == 0 ){
            if(items[index]>=items[index+1]) {
                return items[index]
            }
        }
        else if(index == items.length-1){
           return items[index]
        }
        else {
            if(items[index] >= items[index-1] && items[index] >= items[index+1])
            return items[index]
        }
        index++


    }
}

var items = [1, 2, 6, 4, 5, 4, 3,2, 1]
var perfectCase = [1,8,3,4,3,6,1,4]
//console.log("peek of the items is :" + peakFinder(items))

function peekFinderOptimized(items,start,end){
    if(start == end){
        return items[start]
    }
    var middle = Math.round((start+end)/2)
    if(items[middle] <= items[middle -1]){
        return peekFinderOptimized(items,start,middle)
    }
    else if(items[middle] <= items[middle+1]) {
        return peekFinderOptimized(items,middle,end)
    }   
    else {
        return items[middle]
    }
}
console.log("peek optimized of the items is :" + peekFinderOptimized(perfectCase,0,perfectCase.length-1))