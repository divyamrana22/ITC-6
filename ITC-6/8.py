class ThreeSumFinder:
    def __init__(self, arr):
        self.arr = arr
    
    def find_three_sum(self):
        n = len(self.arr)
        self.arr.sort()
        result = []

        for i in range (len(self.arr) - 2):
            for j in range(i+1,len(self.arr) -1):
                for k in range (j+1,len(self.arr)):
                    if int(self.arr[i]) + int(self.arr[j]) + int(self.arr[k]) == 0 :
                        result.append([self.arr[i],self.arr[j],self.arr[k]])
        
       
        
        return result


# Example usage
input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
three_sum_finder = ThreeSumFinder(input_array)
output = three_sum_finder.find_three_sum()
print(output)
