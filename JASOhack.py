#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy, scipy, IPython.display as ipy, matplotlib.pyplot as ply
import seaborn
import librosa, librosa.display
ply.rcParams['figure.figsize'] = (14, 5)


# In[7]:


audio3sec = 'download.wav'
x, sr = librosa.load (audio3sec)


# In[8]:


ipy.Audio(x, rate=sr)


# In[13]:


ply.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)


# In[ ]:





# In[58]:


librosa.display.specshow(log_cqt, sr=sr, x_axis='time', y_axis='hz', 
                         bins_per_octave=bins_per_octave)
x= librosa.display.specshow(log_cqt, sr=sr, x_axis='time', y_axis='hz', 
                         bins_per_octave=bins_per_octave)


# In[51]:


import numpy as np
import math


# In[59]:


w = np.fft.fft(x)
freqs = np.fft.fftfreq(len(x))

for coef,freq in zip(w,freqs):
    if coef:
        print('{c:>6} * exp(2 pi i t * {f})'.format(c=coef,f=freq))


# In[ ]:





# In[ ]:





# In[ ]:




