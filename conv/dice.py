import numpy as np
def dice_loss(pred, target):
    smooth = 1
    intersection = np.sum(pred*target)
    union = np.sum(pred) + np.sum(target)
    return (intersection + smooth)/(union + smooth)