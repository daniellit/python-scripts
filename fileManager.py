import sys
import os
import shutil

pic_format = ('jpeg','png','gif','jpg')
vid_format = ('avi','flv','wmv','mov','mp4')
aud_format = ('wav','mp3')
doc_format = ('doc','docx','pdf','ppt','pptx','xls','txt', 'xlsx')
exe_format = ('exe')

folder_name = {'picture':'\\Image Files','video':'\\Video Files','audio':'\\Audio Files','doc':'\\Document Files','installer':'\\Installers'}

def create_dir(file_path,**folder_name):
    for key in folder_name.keys():
        directory = file_path + folder_name.get(key)

        if not os.path.exists(directory):
            os.mkdir(directory)
            print(directory)

def search_move(folder_path):
    file_list = os.listdir(folder_path)

    for file in file_list:
        subject = file

        if subject.endswith(pic_format):
            destination = folder_path+'\\Image Files'
        elif subject.endswith(vid_format):
            destination = folder_path+'\\Video Files'
        elif subject.endswith(doc_format):
            destination = folder_path+'\\Document Files'
        elif subject.endswith(aud_format):
            destination = folder_path+'\\Audio Files'
        elif subject.endswith(exe_format):
            destination = folder_path+'\\Installers'
        else:
            continue

        file_path = folder_path+'\\'+subject
        print('des: '+destination)
        print('src: '+file_path)

        if not destination == '' and os.path.exists(destination):
            shutil.move(file_path,destination)

if len(sys.argv)>1:
    path = sys.argv[1]
    create_dir(path,**folder_name)
    search_move(path)
