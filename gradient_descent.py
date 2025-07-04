import numpy as np 
import gradient_utils as gu
import random as rd

def gradient_batch(data, house:set):
    res =[]
    verif =[]
    sorting_hat =[]
    for i in np.unique(house):
        is_house = np.where(house == i, 1, 0)
        poids = np.ones(data.shape[1])
        for _ in range(gu.max_iter):
            sorted_hat = data.dot(poids)
            dist = is_house - gu.sigmoise(sorted_hat)
            gradient = np.dot(data.T,dist)
            poids += gu.pas * gradient
        res.append(sorted_hat)
        verif.append(is_house)
        temp = [i]
        [temp.append(float(x)) for x in poids]
        sorting_hat.append( temp)
    errors = 0
    for i in range(len(sorted_hat)):
        for j in range(len(verif)):
            if verif[j][i] == 1:
                test = []
                max = -12
                for k in range(len(verif)):
                    test.append(res[k][i])
                    if res[k][i] > max:
                        max = res[k][i]
                if res[j][i] != max:
                    print(False)
                    errors +=1
    print(errors, "errors")
    return sorting_hat


def gradient_unit(data, house:set):
    # res =[]
    # verif =[]
    sorting_hat =[]
    for i in np.unique(house):
        is_house = np.where(house == i, 1, 0)
        poids = np.ones(data.shape[1])
        for _ in range(gu.max_iter):
            for j in range(len(data)):
            # print(data[j])
            # for _ in range(gu.max_iter):
                sorted_hat = data[j].dot(poids)
                dist = is_house[j] - gu.sigmoise(sorted_hat)
                gradient = np.dot(data[j].T,dist)
                poids += gu.pas * gradient
            # print("poids", poids)
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


def gradient_mini_batch(data, house:set):
    res =[]
    verif =[]
    sorting_hat =[]
    for i in np.unique(house):
        is_house = np.where(house == i, 1, 0)
        # print(is_house)
        poids = np.ones(data.shape[1])
        for j in range(int(len(data)/50)):
            subdata = data[j * 50: j + 49]
            subhouse = is_house[j * 50: j + 49]
            for _ in range(gu.max_iter):
                sorted_hat = subdata.dot(poids)
                dist = subhouse - gu.sigmoise(sorted_hat)
                gradient = np.dot(subdata.T,dist)
                poids += gu.pas * gradient
            res.append(sorted_hat)
            # print("poids", poids)
        
        verif.append(is_house[0:int(len(data)/50) * 50 -1])
        temp = [i]
        [temp.append(float(x)) for x in poids]
        sorting_hat.append( temp)
    errors = 0
    for i in range(len(sorted_hat)):
        for j in range(len(verif)):
            if verif[j][i] == 1:
                test = []
                max = -12
                for k in range(len(verif)):
                    test.append(res[k][i])
                    if res[k][i] > max:
                        max = res[k][i]
                if res[j][i] != max:
                    print(False)
                    errors +=1
    print(errors, "errors")
    return sorting_hat


def gradient_stochas(data, house:set):
    # res =[]
    # verif =[]
    sorting_hat =[]
    sorted_hat = []
    rd.seed()
    for i in np.unique(house):
        is_house = np.where(house == i, 1, 0)
        # print(is_house)
        poids = np.ones(data.shape[1])
        # print()
        for j in range(int(gu.max_iter/50)):
            subdata =[]
            subhouse =[]
            for k in range(50):
                l = rd.randrange(0, len(data) - 1)
                subdata.append(data[l])
                subhouse.append(is_house[l])
            subdata = np.array(subdata)
            subhouse = np.array(subhouse)
            sorted_hat = subdata.dot(poids)
            dist = subhouse - gu.sigmoise(sorted_hat)
            gradient = np.dot(subdata.T,dist)
            poids += gu.pas * gradient
            # print("poids", poids)
            # res.append(sorted_hat)
            # verif.append(subhouse)
        temp = [i]
        [temp.append(float(x)) for x in poids]
        sorting_hat.append( temp)
    # errors = 0
    # # print("res", res)
    # for i in range(len(res)):
    #     for j in range(len(verif)):
    #         if verif[j][i] == 1:
    #             test = []
    #             max = -12
    #             for k in range(len(verif)):
    #                 test.append(res[k][i])
    #                 if res[k][i] > max:
    #                     max = res[k][i]
    #             if res[j][i] != max:
    #                 # print(False)
    #                 errors +=1
    # print(errors, "errors" , errors/len(res))
    return sorting_hat