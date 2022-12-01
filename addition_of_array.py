# import numpy as np
# a=np.array([[1,2,3],[4,5,6],[2,5,8]])
# b=np.array([3,6,4])
# c=a+b
# print(c)

# import numpy as np
# a=np.array([[1,2,3],[4,5,6]],[[2,5,8],[2,6,7],[[1,2,3],[2,5,8]]])
# b=np.array([[3,6,4],[2,5,6]])
# c=a+b
# print(c)

import numpy as np
a=np.array([[1,2],[2,5,],[6,4],[5,6]])
b=np.sort(a,0,'mergesort')
print(b)