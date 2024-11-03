
""" Python 调用用可执行文件 """
import os
main = "testmain"
if os.path.exists(main):
    # rc, out = commands.getstatusoutput(main)
    # print( 'rc = %d, \nout = %s' % (rc, out))

    f = os.popen(main)  
    data = f.readlines()  
    f.close()  
    print(data) 
 

os.system(main)