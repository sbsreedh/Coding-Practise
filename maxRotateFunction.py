Lets take a small example to understand the situation:

[4,5,3,2,9]

Now,

F(0) = 4 * 0 + 5 * 1 + 3 * 2 + 2 * 3 + 9 * 4 = 53
F(1) = 9 * 0 + 4 * 1 + 5 * 2 + 3 * 3 + 2 * 4 = 31
F(2) = 2 * 0 + 9 * 1 + 4 * 2 + 5 * 3 + 3 * 4 = 44
F(3) = 3 * 0 + 2 * 1 + 9 * 2 + 4 * 3 + 5 * 4 = 52
F(4) = 5 * 0 + 3 * 1 + 2 * 2 + 9 * 3 + 4 * 4 = 50
The crux of this problem is figuring out that the only change between say F(0) and F(1) is that fact that all values except the last (9 in the above example) is multiplied by a number one higher than its previous multiplicant. I have re - wirtten the two lines of above example into a intuitive format. The last number is to be multiplied with zero.

F(0) = 4 * 0 + 5 * 1 + 3 * 2 + 2 * 3 + 9 * 4 = 53
F(1) = 4 * 1 + 5 * 2 + 3 * 3 + 2 * 4 + 9 * 0 = 31

So now to achieve this without looping through the entire array, we can follow the steps given below:
(Defining the O(n) algorithm)

Calculate the sum of the entire array. Lets call if arr_sum

Calculate the F(0) by finding the sum of product of array_val * index. Lets call is it sum_of_products.

Now the interesting part, to calculate F(1) from sum_of_products (which is F(0) ),
i) Perform sum_of_products + arr_sum. (This setp is equivallent to incrementing the multiplier of all the values in the array).
ii) Now from the partial sum subtract the last_val * n (where n is the length of the array). The last element in F(0) is supposed to be multiplied by 0. However in the step i) we essentially increased the multipliers of all array value. So the partial sum reflects the last element * n

Repeat step 3 starting with the last element in the array to the second element in the array.
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        arr_sum = sum(A)
        sum_of_products = 0
        for i,val in enumerate(A):
            sum_of_products+= i*val
        n=len(A)
        maxSum=sum_of_products
        for i in range(1,n):
            sum_of_products+=(arr_sum-A[-i]*n)
            maxSum=max(maxSum,sum_of_products)
        return maxSum
