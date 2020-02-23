import numpy as np

def ex_1_3():
    p_B, p_M = .6, .2
    prior = np.array([p_B, p_M])
    p_K_given_BM = np.array([[.3, .2], [.6, .1]])
    
    print(prior)
    print(p_K_given_BM)

    return 0


if __name__ == '__main__':
    ex_1_3()