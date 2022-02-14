

from black import main
from wordcloud import WordCloud,ImageColorGenerator
import imageio
import jieba

# 1.文本读取与分词

def jieba_(txtfile,stopfile=None):
    content = open(txtfile, 'rb').read()
    if stopfile is not None:
        stop_words = []
        with open(stopfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                stop_words.append(line.strip())

        # jieba 分词
        word_list = jieba.lcut(content)
        words = []
        for word in word_list:
            if word not in stop_words:
                words.append(word)
    
    else:
        # jieba 分词
        words = jieba.lcut(content)
    
    word_cloud = '，'.join(words)
    return word_cloud

# 2.获取图片形状


# 3.词云生成
def create_WC(word_cloud,cloud_mask,output):
    # 定义词云的一些属性
    wc = WordCloud(
        # 背景图分割颜色为白色
        background_color='white',
        # 背景图样
        mask=cloud_mask,
        # 显示最大词数
        max_words=200,
        # 显示中文
        font_path='./fonts/simhei.ttf', 
        # 最大尺寸
        max_font_size=100
    )
    # 词云函数
    x=wc.generate(word_cloud)

    # 调用wordcloud库中的ImageColorGenerator()函数，提取模板图片各部分的颜色
    image_colors = ImageColorGenerator(cloud_mask)

    # 给词云对象按模板图片的颜色重新上色
    wc_color = wc.recolor(color_func=image_colors)
    # 将词云图片导出到当前文件夹
    wc_color.to_file(output)


def main(txtfile,imagepath,output,stopfile=None):
    word_cloud= jieba_(txtfile,stopfile=None)
    cloud_mask=imageio.imread(imagepath)
    create_WC(word_cloud,cloud_mask,output)




    

