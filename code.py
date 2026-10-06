class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n=len(prices)
        i=0
        j=1
        ans=[]
        while i<n and j<n:
            if  prices[j]<=prices[i]:
                o=prices[i]-prices[j]
                ans.append(o)
                i+=1
                j=i+1
                if i==n-1:
                    ans.append(prices[i])
            else:
                j+=1
                if j==n:
                    ans.append(prices[i])
                    i+=1
                    j=i+1
                    if i==n-1:
                        ans.append(prices[i])
        return(ans)
                
        
