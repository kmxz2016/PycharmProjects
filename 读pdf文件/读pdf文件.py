# -*- coding: UTF-8 -*-
import sys
import importlib
reload(sys)
sys.setdefaultencoding('utf-8')

#sudo apt install python-pdfminer

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def readPDF(path,toPath):
    #二进制形式打开
    f = open(path,"rb")

    #创建文档分析器
    parser = PDFParser(f)
    #创建pdf文档
    pdfFile = PDFDocument()

    #链接分析器和文档
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)
    #提供初始密码
    pdfFile.initialize("")

    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #解析数据

        #数据管理器
        manager = PDFResourceManager()
        #创建一个pdf设备对象
        laparams = LAParams()
        device = PDFPageAggregator(manager,laparams=laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manager,device)

        #开始循环处理，每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x,LTTextBoxHorizontal)):
                    with open(toPath,"a") as f:
                        str = x.get_text()
                        print(str)
                        f.write(str+"\n")
path = r"/home/km/PycharmProjects/读pdf文件/11.pdf"
toPath = r"/home/km/PycharmProjects/读pdf文件/a.txt"
readPDF(path,toPath)