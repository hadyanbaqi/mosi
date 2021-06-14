# -*- coding: utf-8 -*-
"""mositugas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GqsEl6xck5gF-RrGb1ZWNANWx12YaFBA
"""

import random
import matplotlib.pyplot as plt
import numpy as np

def rand_walk(x, y, i, j):
  rand = random.uniform(0, 1)
  x_now = x[j][i - 1]
  y_now = y[j][i - 1]
  # Kanan
  if rand <= 0.125:
    x_now += 1
  # Kanan Bawah (serong bawah kanan)
  elif rand <= 0.250:
    x_now += 1
    y_now -=  1
  # Bawah
  elif rand <= 0.375:
    y_now -=  1
  # Bwah Kiri (serong bawah kiri)
  elif rand <= 0.500:
    x_now -= 1
    y_now -=  1
  # Kiri
  elif rand <= 0.625:
    x_now -= 1
  # Kiri Atas (kiri serong atas)
  elif rand <= 0.750:
    x_now -= 1
    y_now +=  1
  # Atas 
  elif rand <= 0.875:
    y_now +=  1
  # Atas Kanan (serong atas kanan)
  else:
    x_now += 1
    y_now +=  1
  x[j][i] = x_now
  y[j][i] = y_now

# init
par_count = 10 #10 Partikel
iter_times = 100  
x = np.zeros((par_count, iter_times))
y = np.zeros((par_count, iter_times))

for i in range(1, iter_times):
  for j in range(par_count):
    rand_walk(x, y, i, j)

plt.figure(figsize=(8,8))
#Plotting 
for j in range(par_count):
  for i in range(1, iter_times):
    plt.plot(x[j], y[j])

plt.title("Random Walk 2D (" + str(iter_times) + " iteration and " + str(par_count) + " Partikel)")
plt.show()