# 使用pandoc转换文档格式

1. 安装pandoc
   
   从[pandoc](https://pandoc.org/installing.html)下载最新的windows安装包即可

* 把word转为markdown
    + 图片多媒体目录：./MediaFolder
    + 输入的word文件: input.docx
    + 输出的markdown文件：output.md

`pandoc --extract-media ./MediaFolder input.docx -o output.md`

* 把markdown转换为word docx格式

`pandoc -o test.docx -f markdown -t docx test.md`