import os
import shutil
import checksumdir

def nuclei_radar():

    with open('sources/templates_sources.txt','r') as repo:
        counter = 0
        for i in repo:          
            counter += 1  
            name = i.split('/')[-1]
            url = "git clone {} templates/{} ".format(i,name).replace('\n','')
            os.system(url)
            print("CLONED [{}/143]".format(counter +1))

        repo.close()

def filter():

    root_dir = 'templates'

    for root ,dirs ,files in os.walk(root_dir):

        for file in files :

            if file.endswith('.yaml'):
                file_path = os.path.join(root,file)
                print(file_path)

                tempelate_database = os.path.join('tempelate_database')


                shutil.copy2(file_path,os.path.join(tempelate_database,file))

    
def collect_dirs_hashs():
    root_dir = 'templates'

    for root ,dirs ,files in os.walk(root_dir):
        for directory in dirs : 

            print(os.path.join(directory)+" : " +checksumdir.dirhash(os.path.join(root ,directory)))





collect_dirs_hashs()