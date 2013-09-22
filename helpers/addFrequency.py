import xml.etree.ElementTree as etree

PATH_IN_SVG = '../pinyinChartTrad.svg'
PATH_OUT_SVG = '../pinyinChartTradFreq.svg'

pCsvg = etree.parse(PATH_IN_SVG)
root = pCsvg.getroot()

pinyinChartDic = {}

### create virtual map of pinyin

for anItem in root[5]:
    x = anItem[0].attrib['x']
    xK = int(0.5+((float(x) - 67.03296) / 38.976378)) 
    y = anItem[0].attrib['y']
    yK = int(0.5+((float(y) - 80.295975) / 42.5196852))

    pinyinChartDic[(xK,yK)] = anItem[0].text
    
### read and create statistics for tones

anEntry=[]
pronDic={}

with open('prons8000.txt', encoding='utf-8') as pron_file:
    for pron_line in pron_file:
        if pron_line.strip(' \n') == '':
            pass
        else:
            for aPron in pron_line.strip().split('/'):
                if aPron.strip('1234') in pronDic: #get data if the entry is there
                    toneCount = pronDic[aPron.strip('1234')]
                else:
                    toneCount = [0,0,0,0,0,0] # create new entry, tone 1,2,3,4,5,Sum

                if '1' in aPron:
                    toneCount[0] += 1
                    toneCount[5] += 1
                elif '2' in aPron:
                    toneCount[1] += 1
                    toneCount[5] += 1
                elif '3' in aPron:
                    toneCount[2] += 1
                    toneCount[5] += 1
                elif '4' in aPron:
                    toneCount[3] += 1
                    toneCount[5] += 1
                else:
                    toneCount[4] += 1
                    toneCount[5] += 1

                pronDic[aPron.strip('1234')]= toneCount

#sort into categories according to number of characters using that sound
pronDicCat = {}

for aPron in pronDic.keys():
    anEntry=pronDic[aPron]
    newEntry = [0,0,0,0,0] #without sum, only 5 tones
    for i in range(5):
        aNumber = anEntry[i]
        if aNumber > 0 and aNumber <= 1:
            newEntry[i]=1
        elif aNumber > 1 and aNumber <= 2:
            newEntry[i] = 2
        elif aNumber > 2 and aNumber <= 4:
            newEntry[i] = 3
        elif aNumber > 4 and aNumber <= 8:
            newEntry[i] = 4
        elif aNumber > 8 and aNumber <= 16:
            newEntry[i] = 5
        elif aNumber > 16:
            newEntry[i] = 6
        else:
            newEntry[i] = 0
    pronDicCat[aPron]=newEntry
    
### create color tiles

def getColor(pinyin,tone):
    colorDic = {
        0:'ffffff', #grey if missing, same for all
        1:'bebebe',
        2:'a5a5a5',
        3:'8c8c8c',
        4:'737373',
        5:'5a5a5a',
        6:'414141',
        }
    if pinyin in pronDicCat:
        return colorDic[pronDicCat[pinyin][tone-1]]
    else:
        return colorDic[0]

for aTile in pinyinChartDic.keys():
    bWidth = '3.85mm'
    bHeight = '4.2mm'

    #first tone, blue
    bStyle='color:#000000;fill:#'+str(getColor(pinyinChartDic[aTile],1))+';fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate'
    bId = str(aTile[0])+'-'+str(aTile[1])+'-T1'
    bX = str(18+(aTile[0]*11))+'mm'
    bY = str(25+(aTile[1]*12)+3.6)+'mm'
    etree.SubElement(root[3],'ns0:rect',{'style':bStyle,'id':bId,'width':bWidth,'height':bHeight,'x':bX,'y':bY})
    #second tone, red
    bStyle='color:#000000;fill:#'+str(getColor(pinyinChartDic[aTile],2))+';fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate'
    bId = str(aTile[0])+'-'+str(aTile[1])+'-T2'
    bX = str(18+(aTile[0]*11)+3.85)+'mm'
    bY = str(25+(aTile[1]*12)+3.6)+'mm'
    etree.SubElement(root[3],'ns0:rect',{'style':bStyle,'id':bId,'width':bWidth,'height':bHeight,'x':bX,'y':bY})
    #third tone, green
    bStyle='color:#000000;fill:#'+str(getColor(pinyinChartDic[aTile],3))+';fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate'
    bId = str(aTile[0])+'-'+str(aTile[1])+'-T3'
    bX = str(18+(aTile[0]*11))+'mm'
    bY = str(25+(aTile[1]*12)+3.6+4.2)+'mm'
    etree.SubElement(root[3],'ns0:rect',{'style':bStyle,'id':bId,'width':bWidth,'height':bHeight,'x':bX,'y':bY})
    #fourth tone, yellow
    bStyle='color:#000000;fill:#'+str(getColor(pinyinChartDic[aTile],4))+';fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate'
    bId = str(aTile[0])+'-'+str(aTile[1])+'-T4'
    bX = str(18+(aTile[0]*11)+3.85)+'mm'
    bY = str(25+(aTile[1]*12)+3.6+4.2)+'mm'
    etree.SubElement(root[3],'ns0:rect',{'style':bStyle,'id':bId,'width':bWidth,'height':bHeight,'x':bX,'y':bY})
    #fifth tone, black, only if existent
    if pinyinChartDic[aTile] in pronDicCat:
        if pronDicCat[pinyinChartDic[aTile]][4]>0:
            bStyle='color:#000000;fill:#'+str(getColor(pinyinChartDic[aTile],5))+';fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate'
            bId = str(aTile[0])+'-'+str(aTile[1])+'-T5'
            bX = str(18+(aTile[0]*11)+1.925)+'mm'
            bY = str(25+(aTile[1]*12)+5.7)+'mm'
            rX = '2.563262'
            rY = '2.563262'
            etree.SubElement(root[3],'ns0:rect',{'style':bStyle,'id':bId,'width':bWidth,'height':bHeight,'x':bX,'y':bY,'rx':rX,'ry':rY})
   #mask for rounded corners
    maskD ='m '+str((18+(aTile[0]*11)-1)*3.5433071)+','+str((25+(aTile[1]*12)+2.6)*3.5433071)+' 0,36.8438 34.375,0 0,-36.8438 -34.375,0 z m 8.15625,3.5625 c 0.17276,-0.017 0.35374,0 0.53125,0 l 17.03125,0 c 2.84009,0 5.125,2.2849 5.125,5.125 l 0,19.5 c 0,2.8401 -2.28491,5.125 -5.125,5.125 l -17.03125,0 c -2.84009,0 -5.125,-2.2849 -5.125,-5.125 l 0,-19.5 c 0,-2.6626 2.00239,-4.8634 4.59375,-5.125 z m 0.875,1.6563 c -2.10559,0 -3.8125,1.7069 -3.8125,3.8125 l 0,18.7812 c 0,2.1056 1.70691,3.8125 3.8125,3.8125 l 16.5,0 c 2.10559,0 3.8125,-1.7069 3.8125,-3.8125 l 0,-18.7812 c 0,-2.1056 -1.70691,-3.8125 -3.8125,-3.8125 l -16.5,0 z'
    mId= str(aTile[0])+'-'+str(aTile[1])+'-mask'
    mStyle ='color:#000000;fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate'
    etree.SubElement(root[3],'ns0:path',{'d':maskD,'style':mStyle,'id':mId})
### write svg
pCsvg.write(PATH_OUT_SVG,'utf-8')
