def searchInsert():
    nums=[1,3,5,6]
    target=7
    print(len(nums) - 1)
    for i in range(len(nums) - 1):
        if target == nums[i]:
            return i

        elif target > nums[i] and target < nums[i + 1]:
            return i + 1

        elif i == (len(nums)- 2):
            return i+2

#
# searchInsert([1,3,5,6],2)
print(searchInsert())viviviuhvfuvvnjvbiuvxcnviuvshvillzcznczxczxhch78954551336564524SSSSSSSSVGD8487844JIJJIJNUH
