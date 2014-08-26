import os
import sys
class Resource_find(object):
    def __init__(self,para1,para2):
        self.rootpath = para1
        self.a,self.extension = os.path.splitext(para2)
        #para2.strip().split('.')[-1]
    def find(self):
        if os.path.exists(self.rootpath):
            openpath = os.path.join(self.rootpath,'index.txt')
            index = open(openpath,'w')
            for root,dirs,files in os.walk(self.rootpath):
                #print root,dirs,files
                for fn in files:
                    files_root,files_extension = os.path.splitext(fn)
                    #print files_extension
                    if files_extension == self.extension:
                        indexwrite = os.path.join(root,fn)
                        print indexwrite
                        index.write(indexwrite+"\r\n")
            index.close()
        else :
            print 1

if __name__ =='__main__':
    if len(sys.argv)<2:
        print "Example:resource_find.py  c:/develop  *.cpp"
        sys.exit(0)
    a = Resource_find(sys.argv[1],sys.argv[2])
    a.find()
