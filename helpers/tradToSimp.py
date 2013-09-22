import xml.etree.ElementTree as etree

PATH_IN_SVG = '../pinyinChartTrad.svg'
PATH_OUT_SVG = '../pinyinChartSimp.svg'

pCsvg = etree.parse(PATH_IN_SVG)
root = pCsvg.getroot()

### create simplified version
trad_simp_dic = {}

### open traditional to simplified table

with open('tradToSimp.txt', mode='r', encoding='utf-8') as trad_simp_file:
    for line in trad_simp_file:
        trad_simp_dic[line.split('\t')[0].strip()]=line.split('\t')[1].strip()

# replace those traditional characters...
for item in root[4]:
    trad = item[0].text
    if trad in trad_simp_dic:
        simp = trad_simp_dic[trad]
    else:
        simp = trad
    if ',' in simp:
        print('please edit: '+simp)
    item[0].text = simp

### write svg

pCsvg.write(PATH_OUT_SVG,'utf-8')
