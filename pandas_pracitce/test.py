import pandas as pd
import numpy as np

gender = pd.DataFrame(data=np.random.randn(18).reshape(9,2), index=range(0, 90, 10), columns=['male', 'female'])
# gender.loc[10, 'male'] = 9
print(gender.index)
for i in gender.index:
    print(gender['male'][i])