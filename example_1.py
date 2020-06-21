# coding:utf-8


from xaizalibs.CMOSanalyzerlib import *


# input の方法
# fits_sample_1.fits を読み込む
input_fits = getArrFits('fits_sample_1.fits')
# 表示してみる
print(input_fits)

# output の方法
# 配列を作成
output_fits_dim_2 = np.random.rand(*(360, 640)) * 100
# 配列 を fits_sample_2.fits に保存
saveAsFits(output_fits_dim_2, 'fits_sample_2.fits')

# 3次元配列を作成
output_fits_dim_3 = np.random.rand(*(10, 360, 640)) * 100
# FITSはn次元の配列を格納できるファイル形式
saveAsFits(output_fits_dim_3, 'fits_sample_3.fits')
