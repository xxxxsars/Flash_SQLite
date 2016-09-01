import csv


st = '''"名字","團體","最近被抽到的日期"
"高坂 穂乃果","μ's",""
"絢瀬 絵里","μ's",""
"南 ことり","μ's",""
"園田 海未","μ's",""
"星空 凛","μ's",""
"西木野 真姫","μ's",""
"東條 希","μ's",""
"小泉 花陽","μ's",""
"矢澤 にこ","μ's",""
"平沢 唯","K-ON!",""
"秋山 澪","K-ON!",""
"田井中 律","K-ON!",""
"琴吹 紬","K-ON!",""
"中野 梓","K-ON!",""
'''

'''
with open('members.csv','w',encoding='utf-8') as fout:
    fout.write(st)
'''

with open('members.csv',encoding='utf-8',newline="") as fin:
    r = csv.DictReader(fin)
    for row in r:
        print('%s of %s'%(row['名字'],row['團體']))