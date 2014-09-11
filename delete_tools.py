import os
import sys
class DT(object):
    def __init__(self,para1,para2,para3):
        self.rootpath = para1
        self.extension = os.path.splitext(para2)[1]
        #print self.extension
        self.filename = para3
        self.filepath = os.path.join(para1,para3)
    def opentext(self):
        if os.path.exists(os.path.join(self.filepath)):
            files = file(self.filepath,'rb')
            self.filesstrlist = files.readlines()
            self.filesstr = "\n".join(self.filesstrlist)
            self.filesstr = self.filesstr+str(self.filename)
    def findfiles(self):
        delete_list = []
        if os.path.exists(self.rootpath):
            listdirs = os.listdir(self.rootpath)
            for fn in listdirs:
                files_extension = os.path.splitext(fn)[1]
                #print (files_extension,self.extension)
                
                if files_extension == self.extension:
                    #print fn
                    if (self.filesstr.find(fn) == -1) :
                        delete_list.append(fn)
            for files in delete_list:
                print files
            bo = raw_input("Do you want to delete all the files?Y/N\t")
            if bo == "Y":
                for files in delete_list:
                    if os.path.exists(files):
                        os.remove(files)
                        print "%s is deleting" % files
                    else :
                        print "%s is not existing" % files

                        
if __name__ =='__main__':
    if len(sys.argv)<3:
        print "Example:resource_find.py  c:/develop  *.cpp"
        sys.exit(0)
    a = DT(sys.argv[1],sys.argv[2],sys.argv[3])
    a.opentext()
    a.findfiles()
                        
                    
        
        
