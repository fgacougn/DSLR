import numpy as np 
import gradient_utils as gu

def gradient_batch(data, house:set):
    # res =[]
    # verif =[]
    sorting_hat =[]
    for i in np.unique(house):
        is_house = np.where(house == i, 1, 0)
        poids = np.ones(data.shape[1])
        for _ in range(gu.max_iter):
            sorted_hat = data.dot(poids)
            dist = is_house - gu.sigmoise(sorted_hat)
            gradient = np.dot(data.T,dist)
            poids += gu.pas * gradient
        # res.append(sorted_hat)
        # verif.append(is_house)
        temp = [i]
        [temp.append(float(x)) for x in poids]
        sorting_hat.append( temp)
    # errors = 0
    # for i in range(len(sorted_hat)):
    #     for j in range(len(verif)):
    #         if verif[j][i] == 1:
    #             test = []
    #             max = -12
    #             for k in range(len(verif)):
    #                 test.append(res[k][i])
    #                 if res[k][i] > max:
    #                     max = res[k][i]
    #             if res[j][i] == max:
    #                 print(True)
    #             else :
    #                 print(False)
    #                 errors +=1
    # print(errors, "errors")
    return sorting_hat