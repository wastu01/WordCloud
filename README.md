# Python Word Cloud「文字雲」文字分析


## 摘要

>文章內容給 Jieba 斷詞，並分析文字產生文字雲，
可推測其文章重要字詞以及核心內容


### 線上文字雲

[https://wordart.com](https://wordart.com)

[http://www.tagxedo.com/gallery.html](http://www.tagxedo.com/gallery.html)

[](https://wordart.com/gnzkixkmt7kz/word-art)


### 文字雲輸出內容：

#### 執行畫面  [點我查看更多](http://bit.ly/01的文字雲分析)


>載入相關套件

```python
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import jieba
import numpy as np
from collections import Counter

```
> Mac OS X 系统文字路徑
>（字體檔案複製貼到 terminal 即可查看）
>
> https://blog.csdn.net/wlher/article/details/98186741


相關檔案在資料夾當中

* txt 資料夾：完整文字檔

* img 資料夾：文字雲圖片

圖片遮罩來源取用自 Unsplash

><span>Photo by <a href="https://unsplash.com/@remiyuan?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Remi Yuan</a> on <a href="https://unsplash.com/s/photos/taiwan?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
>
> <span>Photo by <a href="https://unsplash.com/@thevernon?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Vernon Raineil Cenzon</a> on <a href="https://unsplash.com/s/photos/taiwan?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

