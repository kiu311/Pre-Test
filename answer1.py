def isSubset(array1,array2):
 check=0
 len2=len(array2)
 for x in array1:
  for y in array2:
    if x == y:
      check+=1
 if check == len2:
  state='True'
 else:
  state='False'
 return state
 
