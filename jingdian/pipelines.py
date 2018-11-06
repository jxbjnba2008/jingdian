# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from jingdian.items import JingdianItem
import json
import csv
class JingdianPipeline_json(object):
    # def __init__(self):
    #     self.file = open(r'H:\去哪网爬虫\qunar.json','w+',encoding='utf-8')
    def process_item(self, item, spider):
        file = open(r'H:\去哪网爬虫\%s.json'%item['city'],'a+',encoding='utf-8')
        content = json.dumps(dict(item),ensure_ascii=False) + '\n'
        file.write(content) 
        return item
    # def close_file(self):
    #     file.close()
class JingdianPipeline_csv(object):
    # def __init__(self):
    #     self.file = open(r'H:\去哪网爬虫\qunar.csv','w+',encoding='gb18030',newline='')
    #     self.write = csv.writer(self.file)
    #     self.write.writerow(['name','level','hot','address','num'])
    def process_item(self,item, spider):
        file = open(r'H:\去哪网爬虫\%s.csv'%item['city'],'a+',encoding='gb18030',newline='')
        write = csv.writer(file)
        write.writerow(['name','level','hot','address','num'])
        # write = csv.writer(self.file)
        lists = []
        temp = list(item.values())
        # print(temp)
    #将item数据按'name','level','hot','address','num'行转换成行
        for i in range(15):
            li = []
            for j in range(5):
                try:
                    li.append(temp[j][i])
                except:
                    print('评论人数为0！')
                    li.append(0)
            lists.append(li)
    #将转换好的数据写入文件
        print('正在爬取第%s页'%item['page'][0])
        for content in lists:
            write.writerow(content)
        return item
    # def close_file(self):
    #     self.file.close()