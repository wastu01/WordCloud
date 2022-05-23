#!/usr/bin/env python
# coding: utf-8

import jieba
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
from scipy.ndimage import gaussian_gradient_magnitude


file = open('txt/index.txt', "r", encoding="utf-8")
text = file.read()

jieba.set_dictionary('dict.txt.big.txt')
with open('stopword.txt', 'r', encoding="utf-8") as f:
    stops = f.read().split('\n')
    
terms = []
for sentence in jieba.cut(text):
    if sentence not in stops:
        terms.append(sentence)

dicition = Counter(terms)

# print(Counter(terms))
# data = {
#     'name', 'home'
# }
#
# student_df = pd.DataFrame(data)
#
# print(student_df)
#測試 pandas格式

artDf = pd.DataFrame.from_dict(dicition, orient='index', columns=['詞頻'])
Frequence = artDf.sort_values(by=['詞頻'], ascending=False).head(50)
print(Frequence)
print(artDf.shape)
# print(artDf.dtypes)


#
# artDf = pd.DataFrame(terms, columns=['詞頻'])
# artDf.sort_values(by=['詞頻'], ascending=False)



# with open('outfile', 'w') as w:
#     w.write("The word frequency is " + str(dicition))
font = 'SourceHanSansTW-Regular.otf'
icon = "color"
icon_path = "img/%s.png" % icon

mask_color = np.array(Image.open(icon_path))
mask_color = mask_color[::3, ::3]
mask_image = mask_color.copy()
mask_image[mask_image.sum(axis=2) == 0] = 255

edges = np.mean([gaussian_gradient_magnitude(mask_color[:, :, i]/255., 2) for i in range(1)], axis=0)
mask_image[edges > .08] = 255

wordcloud = WordCloud(max_words=2000,
                      mask=mask_color,
                      font_path=font,
                      max_font_size=45,
                      margin=1,
                      relative_scaling=0)

wordcloud.generate_from_frequencies(frequencies=dicition)
image_colors = ImageColorGenerator(mask_color)
wordcloud.recolor(color_func=image_colors)

plt.figure(figsize=(10, 10), facecolor='w')
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# plt.savefig("render/DCT111.png")
wordcloud.to_file("render/2022-05-23`.png")
file.close()
