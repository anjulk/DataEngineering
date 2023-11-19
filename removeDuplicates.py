def removeDuplicates(nums):
    l = len(nums)
    empty_nums = []
    c=0
    for i in range(l):
       if nums[c]== nums[i] and i!=0:
           pass
       else:
           c=i
           empty_nums.append(nums[c])
           
    return(len(empty_nums), empty_nums)
  
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
