#coding=utf-8

def capstr(name):
    '''
    capstr(name) -> str
    name is a str.
    return a capitalize type of name,or raise TypeError if name is not a str
    '''
    return name.capitalize()




import string
def swastr(name, callback=None):
    '''
    swastr(name, callback=None) -> str
    name is a str.return a str of required tyoe,or a capitalize type if is not required.
    '''
    if callback == None:
        return name.capitalize()
    else:
        return callback(name)    



def getitem(*kargs):
    return kargs



#@吐槽：这个应该可以有多个结果,应该返回一个列表才合理
def shortstr(*kargs):
    '''
    shortstr(*kargs) -> str or None
    return the shortest str in the kargs, or return None if no str in it.
    '''
    #过滤非字符串
    lis = filter(lambda x:isinstance(x,str),kargs)
    #收集长度
    len_lis = [len(x) for x in lis]

    if len_lis:
    		min_index = min(len_lis)
    		return lis[len_lis.index(min_index)]
    return None


def detail(name=None,**kargs):
    '''
    detail(name=None,**kargs) -> str
    name is a str.return a str like'name,key1:value1,key2:value2'    
    '''
    data = []
    for x,y in kargs.items():
        data.extend([',', str(x), ':', str(y)])
   
    info = ''.join(data)
    return '%s%s'%(name,info)

def func(name=None,**kargs):
	lis = ["%s:%s"%(k,v) for k,v in kargs.items()]
	lis.insert(0,name)
	return ','.join(lis)

a = [1,2,3,4,5,6]

b = filter(lambda x :x!=5,a)

b = []
for x in a:
	if x != 5:
		b.append(x)


assert capstr("lilei") == "Lilei"
assert capstr("hanmeimei") == "Hanmeimei"
assert capstr("Hanmeimei") == "Hanmeimei"


assert swastr("lilei") == "Lilei"
assert swastr("LILEI",callback=string.lower) == "lilei"
assert swastr("lilei",callback=string.upper) == "LILEI" 

l = getitem(1,2,3,4,5)

for m in l:
	print m


assert shortstr(222,1111,'xixi','hahahah') == "xixi"
assert shortstr(7,'name','dasere') == 'name'
assert shortstr(1,2,3,4) == None


assert detail("lilei") == "lilei"
assert detail("lilei",years=4) == "lilei,years:4"
assert detail("lilei",years=10,body_weight=20) == "lilei,body_weight:20,years:10"


assert func("lilei") == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,body_weight:20,years:10"