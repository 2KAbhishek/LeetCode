# @param {Integer[]} arr
# @return {Void} Do not return anything, modify arr in-place instead.
def duplicate_zeros(arr)
    newArr = []
    arr.each do |i|
        unless newArr.length >= arr.length
            if i == 0 and (newArr.length + 2) <= arr.length
                newArr.insert(newArr.length, i)
                newArr.insert(newArr.length, i)
            else
                newArr.insert(newArr.length, i)
            end
        end
    end
    (0...arr.size).each{|i| arr[i] = newArr[i]}
end