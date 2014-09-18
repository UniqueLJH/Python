import os
import shutil
import sys
import Image
class Resource_copy(object):
    def __init__(self,para1,para2,para3,para4):
        self.rootpath = para1
        self.name = para2
        self.a,self.extension = os.path.splitext(para3)
        self.targetpath = para4
        self.jpglist= ['.png','.jpg','.jpeg','.gif','.bmp']
    def exist_targetpath(self):
        if os.path.exists(self.targetpath):
            recover__bo = raw_input('targetpath already exists,Do u want to recover it?(Y/N)')
            if recover__bo == 'Y' :
                shutil.rmtree(self.targetpath)
                os.makedirs(self.targetpath)
        else:
            os.makedirs(self.targetpath)
    def copy(self):
        logfile = open('logfile.txt','w')
        for root,dirs,files in os.walk(self.rootpath):
            
            r = root.strip().split('\\')[-1]
            #print root,dirs,files,r
            if r == self.name:
                for fn in files:
                    files_path,files_extension = os.path.splitext(fn)
                    #.strip().split('.')[1]
                    if files_extension == self.extension:
                        a = os.path.join(root,fn)
                        b = os.path.join(self.targetpath,fn)
                        if os.path.exists(b):
                            asize =os.path.getsize(a)
                            bsize = os.path.getsize(b)
                            if asize == bsize :
                                print "copy \"%s\"  ok(exist)"%(a)
                                logwrite = "copy \""+a+"\" ok (exist)\r\n"
                                logfile.write(logwrite)
                            else:
                                if (files_extension in self.jpglist):
                                    ima = Image.open(a)
                                    imb = Image.open(b)
                                    if ima.size = imb.size :
                                        print "copy \"%s\"  failed(exist and is same picture)"%(a)
                                        logwrite = "copy \""+a+"\" failed(exist and is same picture)\r\n"
                                        logfile.write(logwrite)
                                    else :
                                        print "copy \"%s\"  failed(exist but not same)"%(a)
                                        logwrite = "copy \""+a+"\" failed(exist but not same)\r\n"
                                        logfile.write(logwrite)
                                else:                                
                                    print "copy \"%s\"  failed(exist but not same)"%(a)
                                    logwrite = "copy \""+a+"\" failed(exist but not same)\r\n"
                                    logfile.write(logwrite)
                        else:
                            open(b,"wb").write(open(a,"rb").read())
                            print "copy \"%s\"  ok"%(a)
                            logwrite = "copy \""+a+"\" ok\r\n"
                            logfile.write(logwrite)
        logfile.close()                

if __name__ =='__main__':
    if len(sys.argv)<4:
        print "Example:resource_copy.py  c:\game  resource  *.png  c:\game_resource"
        sys.exit(0)
    a = Resource_copy(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    a.exist_targetpath()
    a.copy()
    
