import os
import sys
import json
class EJR(object):
    def __init__(self,para1,para2,para3):
        self.rootpath = para1
        self.change1 = para2
        self.change2 = para3
    def change(self):
        if os.path.exists(self.rootpath):
            listdirs = os.listdir(self.rootpath)
            for fn in listdirs:
                #print fn
                files_extension = fn.strip().split('.')[-1]
                if files_extension == 'ExportJson':
                    f = file(os.path.join(self.rootpath,fn),'rb')
                    s = json.load(f)
                    #print s
                    if s.has_key('config_file_path'):
                        l1 = []
                        l1.append(self.change1)
                        s['config_file_path'] = l1
                    if s.has_key('config_png_path'):
                        l2 = []
                        l2.append(self.change2)
                        s['config_png_path'] = l2
                    f.close()
                    
                    text = json.dumps(s,separators=(',',':'))
                    #print text
                    f = file(os.path.join(self.rootpath,fn),'w')
                    f.write(text)
                    f.close()
                    print os.path.join(self.rootpath,fn)+' replace success'
                    
                
    
if __name__ =='__main__':
    if len(sys.argv)<3:
        print "Example:resource_find.py  c:/develop  *.cpp"
        sys.exit(0)
    a = EJR(sys.argv[1],sys.argv[2],sys.argv[3])
    a.change()
