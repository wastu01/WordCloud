# Python Word Cloud「文字雲」文字分析

#### 更新：
更新至 python3.9 版本使用 counter 需加入
#### from collections import Counter

#### pandas 排序次數問題：
[transform-a-counter-object-into-a-pandas-dataframe](https://stackoverflow.com/questions/31111032/transform-a-counter-object-into-a-pandas-dataframe)
## 摘要

練習如何斷詞：
[https://github.com/wastu01/Jieba-ChinsesWord](https://github.com/wastu01/Jieba-ChinsesWord)

>文章內容給 Jieba 斷詞，並分析文字產生文字雲，
可推測其文章重要字詞以及核心內容


### 線上文字雲

[https://wordart.com](https://wordart.com)

[http://www.tagxedo.com/gallery.html](http://www.tagxedo.com/gallery.html)

[](https://wordart.com/gnzkixkmt7kz/word-art)


### 文字雲輸出內容：

#### 執行畫面 

![](https://static.coderbridge.com/img/mrwang01/afa9d18930bc46e7bcc6bd07362d3946.png)


>載入相關套件(requirement)

```python
import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from scipy.ndimage import gaussian_gradient_magnitude

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

延伸應用：

[線上爬取使用者想查的關鍵字製作成文字雲](http://bit.ly/Mr01Medium)

