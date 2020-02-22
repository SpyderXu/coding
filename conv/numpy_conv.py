import numpy as np
def conv_op(x, w, b, stride, padding):
    NI, CI, WI, HI = x.shape
    CO, CI, K, K = w.shape
    NO = NI
    WO = int((WI - K + 2*padding)/stride)
    HO = int((HI - K + 2*padding)/stride)
    xo = np.zeros((NI, CO, HO, WO))
    xi = np.zeros((NI, CI, WI+2*padding, HI+2*padding))
    xi[:, :, padding:-padding, padding:-padding] = x
    
    for k in range(CO):
        for i in range(HO):
            for j in range(WO):
                xo[:,k,i,j] = np.sum(xi[:, :, i-K//2:x+K//2, j-K//2:j+K//2]*w[k,:,:,:], axis = (1,2,3))
                xo[:,k,i,j] += b[k]
    return xo
            
    