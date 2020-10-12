# import docx
# import pandas as pd
# import random
#
# wordpath=r'D:\文档\OneDrive-wyx\OneDrive - wuyaoxue\亚信实习\工作\公安三期项目\规格.docx'
# doc=docx.Document(wordpath)
#
#
# def set_head():
#     i = 0
#
#     while True:
#         try:
#             if doc.paragraphs[i].style.name == 'Heading 4':
#
#                 # print('i', i)
#                 para_text = doc.paragraphs[i].text
#                 print(para_text)
#
#
#                 doc.paragraphs[i+1].insert_paragraph_before(text='功能描述',style='Heading 5')
#                 doc.paragraphs[i+2].insert_paragraph_before(text='外部信息',style='Heading 5')
#                 doc.paragraphs[i+3].insert_paragraph_before(text='内部信息',style='Heading 5')
#                 doc.paragraphs[i+4].insert_paragraph_before(text='数据处理',style='Heading 5')
#                 doc.paragraphs[i+5].insert_paragraph_before(text='系统输出',style='Heading 5')
#                 doc.paragraphs[i+6].insert_paragraph_before(text='查询',style='Heading 5')
#                 doc.paragraphs[i+7].insert_paragraph_before(text='生产内部数据',style='Heading 5')
#
#
#             length = len(doc.paragraphs)
#             if i+1 == length:
#                 break
#             else:
#                 i += 1
#         except BaseException as e :
#             print(e)
#             break
#             # doc.save(r'F:\pythonPrj\Asiainfo\word\test.docx')
#
# set_head()
# doc.save(r'F:\pythonPrj\Asiainfo\word\test.docx')


def rotate(nums, k):
    start = 0
    end = len(nums) - 1
    k = k % len(nums)

    reverse(nums, start, end)
    reverse(nums, start, k - 1)
    reverse(nums, k, end)

    return nums


def reverse(nums, start, end):
    while start < end:
        t = nums[start]
        nums[start] = nums[end]
        nums[end] = t
        # print(nums)
        start += 1
        end -= 1


A1='天天基金,蚂蚁财富,掌上基金,现金宝,滚雪球基金,同花顺爱基金,e钱包,嘉实理财嘉,南方基金,华夏基金管家,广发基金,天虹爱理财,利得基金,中欧钱滚滚,银华生利宝,富国富钱包,博时基金,招商招钱宝,工银现金快线,鹏华A加钱包,建信基金,中银基金,安信基金,兴全基金,国泰基金,国投瑞银,大成基金,景顺长城基金,交银基金,基金E站,广大保德信基金,融通基金,华安基金,华商基金,诺安基金,东方基金,华泰柏瑞,长信基金,农银汇理基金,长盛基金,贝壳APP'.split(',')
A2='ok车险,保险大咖,保险驾到,快保,平安保险商城,i云保,平安健康,水滴保险,梧桐树保险,向日葵宝信啊,小贝保险,小智保险,阳光保险,阳光惠生活,最惠保,太平洋保险,平安金管家,平安车主,国寿e宝,神行太保,众安,中国人保,泰康在线,平安健康,大象保险,唯彩看球,付临门,还呗,好分期,来分期,趣花分期,时光分期,我爱卡,平安证券,华泰证券,财富证券,智远一户通,国泰君安,银河证券,广发证券,海通证券'.split(',')
i=0
j=0

for n in range(len(A1)):
    for i in range(len(A1)):
       print(i,A1[i],A2[i])
    rotate(A2,1)

