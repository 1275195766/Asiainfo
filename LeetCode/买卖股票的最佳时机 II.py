#coding:utf8
from typing import List


class Solution:
    #暴力法
    def maxProfit(self, prices: List[int]) -> int:
        def calculate(prices,s):
            if len(prices)==s:
                return 0
            max=0
            profit=0
            for start in range(s,len(prices)):
                maxprofit=0
                for i in range(start+1,len(prices)):
                    if prices[start]<prices[i]:
                        profit=calculate(prices,i+1)+prices[i]-prices[start]
                    if profit>maxprofit:
                        maxprofit=profit
                if maxprofit>max:
                    max=maxprofit
            return max



        return calculate(prices,0)


    #峰谷法
    def maxProfit1(self,prices: List[int]) -> int:
        # print(len(prices))
        i=0
        valley=prices[0]
        peak=prices[0]
        maxprofit=0
        while i<len(prices)-1:
            while i<len(prices)-1 and prices[i]>=prices[i+1]:
                i+=1
            valley=prices[i]
            while i<len(prices)-1 and prices[i]<=prices[i+1]:
                i+=1
            peak=prices[i]

            maxprofit+=peak-valley
        return maxprofit


    #一次遍历,贪心算法
    def maxProfit2(self,prices: List[int]) -> int:
        maxprofit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxprofit+=prices[i]-prices[i-1]

        return maxprofit



if __name__=="__main__":
    a=Solution().maxProfit2([7, 1, 5, 3, 6, 4])
    print(a)
