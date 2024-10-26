# 将word转为markdown
## 图片保存路径 ./myMediaFolder
## 输入的docx input.docx
## 输出的md output.md
pandoc --extract-media ./myMediaFolder input.docx -o output.md

# 使用pandoc转换文档格式

1. 安装pandoc
   
   从[pandoc](https://pandoc.org/installing.html)下载最新的windows安装包即可

* 把word转为markdown
    + 图片多媒体目录：./MediaFolder
    + 输入的word文件: input.docx
    + 输出的markdown文件：output.md

`pandoc --extract-media ./MediaFolder input.docx -o output.md`

# 把markdown转换为word docx格式

pandoc -o test.docx -f markdown -t docx test.md

cd .\apulis-5g-ai-manufacturing-platform-docs\docs\zh_CN\ 
pandoc -o test.docx -f markdown -t docx 依瞳智慧工业平台用户手册-v2.md

