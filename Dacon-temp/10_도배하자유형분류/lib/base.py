import os
def mkdir(path):
    if not os.path.exists(path):
        print("folder created: {}".format(path))
        os.mkdir(path)

import numpy as np
def label_encoder(label):
    label = list(label)
    new_label = [
        0  if l=='가구수정' else
        1  if l=='걸레받이수정' else
        2  if l=='곰팡이' else
        3  if l=='꼬임' else
        4  if l=='녹오염' else
        5  if l=='들뜸' else
        6  if l=='면불량' else
        7  if l=='몰딩수정' else
        8  if l=='반점' else
        9  if l=='석고수정' else
        10 if l=='오염' else
        11 if l=='오타공' else
        12 if l=='울음' else
        13 if l=='이음부불량' else
        14 if l=='창틀,문틀수정' else
        15 if l=='터짐' else
        16 if l=='틈새과다' else
        17 if l=='피스' else
        18 if l=='훼손' else
        np.nan for l in label
    ]
    return new_label

def label_decoder(label):
    new_label = [
        '가구수정' if l==0 else
        '걸레받이수정' if l==1 else
        '곰팡이' if l==2 else
        '꼬임' if l==3 else
        '녹오염' if l==4 else
        '들뜸' if l==5 else
        '면불량' if l==6 else
        '몰딩수정' if l==7 else
        '반점' if l==8 else
        '석고수정' if l==9 else
        '오염' if l==10 else
        '오타공' if l==11 else
        '울음' if l==12 else
        '이음부불량' if l==13 else
        '창틀,문틀수정' if l==14 else
        '터짐' if l==15 else
        '틈새과다' if l==16 else
        '피스' if l==17 else
        '훼손' if l==18 else
        'NaN' for l in label
    ]
    return new_label