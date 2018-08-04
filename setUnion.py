class Set():
    def __init__(self,list):
        self.collection = list
    def values(self):
        return self.collection 
    def size(self):
        return len(self.collection)
    def has(self,ele):
        flag = False
        for i in range(0,self.size()):
            if(self.collection[i] == ele):
                flag = True
                break
        return flag     
    def union(self,setB):
        values = setB.values()
        for i in range(0,len(values)):
            if not self.has(values[i]):
                self.collection.append(values[i])
      
myset =Set([1,2,3,5])
secondSet = Set([3,4,5])
myset.union(secondSet)
print(myset.values())