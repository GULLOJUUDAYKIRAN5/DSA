 def climb(n,dict):
            if n in dict:
                return dict[n]
            if n==1: 
                return 1
            if n ==2: 
                return 2
            dict[n]=climb(n-1,dict) + climb(n-2,dict)
            return dict[n]
    
        dict={}
        return climb(n,dict)
        #  dp 
        