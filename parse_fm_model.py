path = r"C:\Users\XXX\Desktop\fm_model.txt"
count = 0
bias = 0
w = {}
w_fm = {}
with open(path, 'r') as f:
    lines = f.readlines()
    for c,line in enumerate(lines):
        tmp = line.strip().split(' ')
        if c == 0:
            bias = float(tmp[1])
        else:
            key = tmp[0]
            w[key]=float(tmp[1])
            w_fm[key] = [float(i) for i in tmp[2:10]]       
            # count += 1
            # if count > 10:
            #     break

def get_feat(s):
    ss = s.split(" ")
    label = ss[0]
    features = [i.split(':')[0] for i in ss[1:]]
    print(features)
    print(label)
    return features


import math
def predict(x,fm_dim = 8):
    raw_y = bias
    # calculate the bias contribution
    # calculate the first order contribution.
    for i in x:
        raw_y += w[i]
    len_x = len(x)
    for i in range(len_x):
        for j in range(i + 1, len_x):
            for k in range(fm_dim):
                raw_y += (w_fm.get(x[i])[k]) * (w_fm.get(x[j])[k])
    return 1. / (1. + math.exp(- max(min(raw_y, 35.), -35.)))
