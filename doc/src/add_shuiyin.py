#=============================================
# @Time    : 2021-01-24
# @Author  : AXYZdong
# @FileName: PDFset.py
# @Software: Python IDE
#=============================================

from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import os

def create_watermark(watermark_text, watermark_file="watermark.pdf"):
  """水印信息"""
  # 默认大小为21cm*29.7cm
  c = canvas.Canvas(watermark_file, pagesize=(30*cm, 30*cm))
  # 移动坐标原点(坐标系左下为(0,0))
  c.translate(10*cm, 5*cm)

  # 设置字体
  c.setFont("Helvetica", 30)
  # 指定描边的颜色
  c.setStrokeColorRGB(0, 1, 0)
  # 指定填充颜色
  c.setFillColorRGB(0, 1, 0)
  # 旋转45度,坐标系被旋转
  c.rotate(30)
  # 指定填充颜色
  c.setFillColorRGB(0, 0, 0, 0.1)
  # 设置透明度,1为不透明
  # c.setFillAlpha(0.1)
  # 画几个文本,注意坐标系旋转的影响
  for i in range(5):
    for j in range(10):
      a=10*(i-1)
      b=5*(j-2)
      c.drawString(a*cm, b*cm, watermark_tex t)
      c.setFillAlpha(0.1)
  # 关闭并保存pdf文件
  c.save()
  return watermark_file


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
  """把水印添加到pdf中"""
  pdf_output = PdfFileWriter()
  input_stream = open(pdf_file_in, 'rb')
  pdf_input = PdfFileReader(input_stream, strict=False)

  # 获取PDF文件的页数
  pageNum = pdf_input.getNumPages()

  # 读入水印pdf文件
  pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
  # 给每一页打水印
  for i in range(pageNum):
    page = pdf_input.getPage(i)
    page.mergePage(pdf_watermark.getPage(0))
    page.compressContentStreams() # 压缩内容
    pdf_output.addPage(page)
  pdf_output.write(open(pdf_file_out, 'wb'))

if __name__ == '__main__':
    import os
    file_path = r"C:\Users\Admin\workspace\工业质检平台文档"
    file_name = '依瞳智能工业平台快速指南.pdf'
    watermark_text = "Apulis Tech"
    watermark_file=os.path.join(file_path, "watermark.pdf")
    pdf_file_mark = create_watermark(watermark_text,  watermark_file)
    pdf_file_in = os.path.join(file_path,file_name)
    pdf_file_out = os.path.join(file_path,"-".join(["shuyin", file_name]))
    add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
    