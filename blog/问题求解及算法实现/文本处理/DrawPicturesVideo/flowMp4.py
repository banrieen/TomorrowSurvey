""" 使用python3+opencv3.3.1环境将视频流保存为本地视频文件，具体内容如下

1、利用opencv中的VideoCapture类获取视频流的链接，通过cv2的方法得到该视频流的帧数和每帧大小。

2、使用VideoWriter类进行视频编码

3、通过VideoCapture的read()方法进行视频流解码成每一帧

4、获取到每一帧frame，我们就可以对该帧做图像算法（例如识别、图像加强、灰度变换等）
 """
import cv2 
from matplotlib import pyplot as plt 
  
#通过cv2中的类获取视频流操作对象cap 
cap = cv2.VideoCapture('rtsp://admin:passwd@10.130.10.111:554/MPEG-4/ch1/main/av_stream') 
#调用cv2方法获取cap的视频帧（帧：每秒多少张图片） 
fps = cap.get(cv2.CAP_PROP_FPS) 
print(fps) 
#获取cap视频流的每帧大小 
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) 
print(size) 
  
#定义编码格式mpge-4 
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2') 
#定义视频文件输入对象 
outVideo = cv2.VideoWriter('saveDir.avi',fourcc,fps,size) 
  
#获取视频流打开状态 
if cap.isOpened(): 
  rval,frame = cap.read() 
  print('ture') 
else: 
  rval = False
  print('False') 
  
tot=1
c=1
#循环使用cv2的read()方法读取视频帧 
while rval: 
  rval,frame = cap.read() 
  cv2.imshow('test',frame) 
  #每间隔20帧保存一张图像帧 
  # if tot % 20 ==0 : 
  #   cv2.imwrite('cut/'+'cut_'+str(c)+'.jpg',frame) 
  #   c+=1 
  tot+=1
  print('tot=',tot) 
  #使用VideoWriter类中的write(frame)方法，将图像帧写入视频文件 
  outVideo.write(frame) 
  cv2.waitKey(1) 
cap.release() 
outVideo.release() 
cv2.destroyAllWindows()