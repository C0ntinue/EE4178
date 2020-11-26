#-*- coding: utf-8 -*-


import torch
import torchvision
import torch.nn as nn
import torchvision.transforms as transforms
import matplotlib.pyplot as plt


class TypeData(Dataset):
  '''
### Digit�� ��� label�� 0��, ###
### Letter�� ��� label�� 1�� ###
### return�ϴ� class�Դϴ�. ###

��� ����:
train_data = TypeData(train=True)
test_data = TypeData(train=False)
  '''
  def __init__(self,train):
    super(TypeData, self).__init__()
    self.digit = 10
    self.letter = 46
    self.train = train

    self.data = torchvision.datasets.EMNIST(root='./',
                                        split='bymerge',
                                        train=self.train,
                                        transform=transforms.ToTensor(),
                                        download=True)

  def __getitem__(self, index):
    if self.data[index][1] <= self.digit:
      label = 0.
    else:
      label = 1.
    return self.data[index][0], label

  def __len__(self):
    return len(self.data)



### train �Ǵ� test dataset�� ���Ͽ�, num�� ����ŭ subplot�� �����ִ� �Լ��Դϴ�.
def image_show(dataset, num):
  fig = plt.figure(figsize=(30,30))

  for i in range(num):
    plt.subplot(1, num, i+1)
    plt.imshow(dataset[i][0].squeeze())
    plt.title(dataset[i][1])