import logging

import PyPDF2
import datetime


def search_my_file(input_dir,ext):
    import os
    """this func takes the path of the directory in which text files will be searched"""

    files_list=[]
    try:
        os.chdir(input_dir)
        for root,dire,files in os.walk(input_dir,topdown=True):
            for f in files:
                if f.endswith(ext)==True:
                    files_list.append(f)
        return files_list
    except Exception as e:
        logging.error("error occured in search_my_file"+str(e))

def merge_pdf(input_dir):
    all_files=search_my_file(input_dir,".pdf")
    current=datetime.datetime.now()
    current=current.strftime("%d%m%Y%H%M%S")
    print(current)
    try:
        file_merger=PyPDF2.PdfFileMerger()
        for i in all_files:
            read_pdf=PyPDF2.PdfFileReader(input_dir+"\\"+str(i),"rb")
            file_merger.append(read_pdf)
        new_file=open(f"{input_dir}" + "\\" +str(current)+'mergedfile.pdf',"wb")
        file_merger.write(new_file)

        return new_file.name
    except Exception as e:
        logging.error("error occured in merge_pdf"+str(e))

# merger = PdfFileMerger()
# for filename in filenames:
#     merger.append(PdfFileReader(file(filename, 'rb')))

# merger.write("document-output.pdf")
