def decideone(pars, distances):

    import numpy as np
    import pandas as pd

    # pars = np.random.normal(0, 0.1, 15)
    pars1 = np.random.normal(0, 0.1, 15)
    pars2 = np.random.normal(0, 0.1, 15)

    # pars = np.array([pars1, pars2])

    # distances = [1,2,3,4,5]
    # print(distances * 3)
    dist6 = distances * 3
    # print(pars * dist6)
    # print(pars * dist6 * neron1)
    # a =
    # print(a)
    # a =
    # df = pd.DataFrame(a, index=[1,2,3,4,5] * 6)
    df = pd.DataFrame(np.transpose(pars * dist6))
    df["ind"] = [1,2,3] * 5
    # print(df)
    df2 = df.groupby(['ind']).sum()
    # print(df2)
    df3 = pd.DataFrame(df2)

    return(df3.idxmax())

# pars1 = np.random.normal(0, 0.1, 15)
# pars2 = np.random.normal(0, 0.1, 15)
#
# pars1 = np.array([pars1, pars2])
# distances1 = [1,2,3,4,5]
# decideone(pars1, distances1)