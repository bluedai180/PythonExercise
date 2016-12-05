# coding = utf-8
result = []
pinyin = []
pinyin_panduan = []

data = open("Files/rawdict_utf16_65105_freq.txt", 'r', encoding='utf-8')
for x in data.readlines():
    result.append(x.split(' '))

#print(result)
for y in result:
    pinyin.append(y[3])
    if len(y) == 5:
        pinyin.append(y[3] + y[4])

pinyin_panduan = list(set(pinyin))
str_text = []

for z in pinyin_panduan:
    for item in result:
        if len(item) == 4:
            if z == item[3]:
                str_text.append(item[0])
        #print('const unsigned char PY_mb_%s []= {"%s"};' % (z, list(set(list(str_text)))))
    print(str_text)
        # elif len(item) == 5:
        #     if z == item[3] + item[4]:
        #         print('const unsigned char PY_mb_%s_%s []= {"%s"};' % (item[3], item[4], item[0]))


#print(pinyin_panduan)

data.close()