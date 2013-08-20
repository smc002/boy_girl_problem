#coding=utf-8

boy_s = '男'
girl_s = '女'

print('\nBoy is represent by {}, girl is represent by {}.\n'.format(boy_s, girl_s))

pos = 1
b_n = 0
g_n = 0
for i in range(1000):
    pos = pos / 2
    b_n = b_n + 1 * pos
    g_n = g_n + i * pos
    print('第{}个家庭组成：'.format(i+1), end=': ')
    print(girl_s*i + boy_s)
    print( 'possibility of this family: ', pos)
    print('Efficient boy number till now: ', b_n)
    print('Efficient girl number till now: ', g_n)
    print()
    input('Press ENTER to continue')
