import numpy as np
def nms_py(dets, thresh, eps = 1e-6):
    xmin = dets[:,0]
    ymin = dets[:,1]
    xmax = dets[:,2]
    ymax = dets[:,3]
    score = dets[:,4]
    area = (ymax - ymin)*(xmax - xmin)
    index = score.argsort()
    keep = []
    while len(index)!=0:
        ind = index[0]
        keep.append(ind)
        inter_xmin = np.maximum(xmin[ind], xmin[index[1:]])
        inter_ymin = np.maximum(ymin[ind], ymin[index[1:]])
        inter_xmax = np.minimum(xmax[ind], xmax[index[1:]])
        inter_ymax = np.minimum(ymax[ind], ymax[index[1:]])
        inter_w = np.maximum(inter_xmax - inter_xmin, 0.0)
        inter_h = np.maximum(inter_ymax - inter_ymin, 0.0)
        inter_area = inter_w*inter_h
        union_area = area[ind] + area[index[1:]]
        iou = inter_area/(union_area + 1e-6)
        keep_index = np.where(iou < thresh)[0]
        index = index[1:][keep_index]