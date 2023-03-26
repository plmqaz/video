import os,sys
datanames = os.listdir('d:/Works/')
for dataname in datanames:
    if dataname.endswith(".srt") or dataname.endswith(".mp3") or dataname.endswith(".wav") or dataname.endswith(".avi") or dataname.endswith(".kax"):
        os.remove("d:/Works/{}".format(dataname))
        print(dataname)