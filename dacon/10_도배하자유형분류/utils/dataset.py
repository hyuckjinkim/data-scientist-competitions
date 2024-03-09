import numpy as np
import pandas as pd
import itertools
import cv2
from tqdm.auto import tqdm, trange

import torch
from torch.utils.data import Dataset

import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2

# brainAI 이희원님 공유내용
# (참조) https://dacon.io/competitions/official/236082/codeshare/7891?page=1&dtype=recent
class ImageDataset(Dataset):
    def __init__(self, img_path_list, label_list=None, augmentations=None, transforms=None):
        self.label_list = label_list
        augmentation_ref_rate = 0.05
        
        if augmentations is not None:
            percentage = pd.Series(label_list).value_counts() / len(label_list)
            augmentation_info = percentage[percentage<augmentation_ref_rate]
            augmentation_info = np.sqrt(1/augmentation_info) # 증강시킬 개수를 np.sqrt(1/비중)으로 계산
            augmentation_label = augmentation_info.index
            augmentation_n = augmentation_info.values
            augmentation_n = [int(n) for n in augmentation_n] # float -> int

            aug_combinations = []
            for i in range(1,len(augmentations)+1):
                aug_combinations += list(itertools.combinations(augmentations, i))
            max_n_augmentation = len(aug_combinations) # 가능한 augmentation 조합의 수
            max_n_augmentation = int(max_n_augmentation/5)

        self.feature = []
        if label_list is not None:
            self.label = []
        pbar = trange(len(img_path_list),desc='Read Image and Augmentation')
        for i in pbar:
            # (1) raw image
            image = cv2.imread(img_path_list[i])
            self.feature.append(image)
            if label_list is not None:
                label = label_list[i]
                self.label.append(label)
        
            # (2) augmentationed image
            if augmentations is not None:
                # new image
                if label in augmentation_label:
                    augmentation_idx = np.where(augmentation_label==label)[0][0]
                    n_augmentation = augmentation_n[augmentation_idx]
                    n_augmentation = min(n_augmentation,max_n_augmentation)
                    for k in range(n_augmentation):
                        pbar.set_description(f'Image Load & Augmentations ({k+1}/{n_augmentation})')
                        new_image = augmentations(image=image)['image']
                        self.feature.append(new_image)
                        if label_list is not None:
                            self.label.append(label)
        
        self.final_feature = []
        # (3) transformed image
        for image in tqdm(self.feature,desc='Transform'):
            if transforms is not None:
                image = transforms(image=image)['image']
            self.final_feature.append(image)
            
        del self.feature

    def __getitem__(self, index):
        if self.label_list is not None:
            return self.final_feature[index], self.label[index]
        else:
            return self.final_feature[index]
        
    def __len__(self):
        return len(self.final_feature)