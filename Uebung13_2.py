import biostat as bs
import numpy as np

success=False
nums=[]
while success==False:
    z=input('Please enter your numbers. End your list by just pressing Enter.')
    if z=='':
        success=True
    else:
        try:
            z=float(z)
            nums.append(z)
        except:
            print('Your input is no valid number.')
print(nums)
print('BS Mean: '+str(bs.mean(nums)))
print('NP Mean: '+str(np.mean(nums)))
print('BS Variance: '+str(bs.var(nums)))
print('NP Variance: '+str(np.var(nums)))
print('BS Standard Deviation: '+str(bs.std(nums)))
print('NP Standard Deviation: '+str(np.std(nums)))