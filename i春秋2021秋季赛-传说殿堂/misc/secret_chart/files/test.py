# coding:utf8
# python3

from PIL import Image

the_file = open('01.txt', 'r')
the_matrix = the_file.read().strip().split('\n')
the_file.close()


im = Image.new('RGB', (24, 24), (255,255,255))  # 白色
pic = im.load()
for i in range(24):
    for j in range(24):
        if the_matrix[i][j] == '1':
            pic[j, i] = (0, 0, 0)  # 黑色

im.save('a.jpg')
