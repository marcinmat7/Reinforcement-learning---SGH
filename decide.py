import numpy as np
import pandas as pd
import math

def decidetwo(pars, pars2, distances):


    # print(pars)

    # distances = [1,2,3,4,5]
    # print(distances * 6)
    dist6 = distances * 6
    # print(pars * dist6)
    # print(pars * dist6 * neron1)
    a = pars * dist6
    # print(a)
    a = np.transpose(a)
    # df = pd.DataFrame(a, index=[1,2,3,4,5] * 6)
    df = pd.DataFrame(a)
    df["ind"] = [1,2,3,4,5,6] * 5

    # print(df)

    df2 = df.groupby(['ind']).sum()
    # type(df2)
    # math.cos(1,2)

    layer1 = pd.Series(df2.iloc[:,0])
    layer1 = 1 / (1 + np.exp(-layer1))

    distances2 = layer1.astype(float)
    distances3 = np.array(distances2, float)

    dist3 = list(distances3) * 3
    a = pars2 * dist3
    # print(a)
    a = np.transpose(a)
    # df = pd.DataFrame(a, index=[1,2,3,4,5] * 6)
    df = pd.DataFrame(a)
    df["ind"] = [1,2,3] * 6
    df2 = df.groupby(['ind']).sum()
    # print(df2.idxmax())
    return(df2.idxmax())

