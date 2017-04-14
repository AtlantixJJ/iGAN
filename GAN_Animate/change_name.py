import os
import argparse
parser = argparse.ArgumentParser('Change name for images.')
parser.add_argument('--dir',default='./')
args = parser.parse_args()
filelist = os.listdir(args.dir)
cnt = 1
tot = len(filelist)
print(tot)
for i,f in enumerate(filelist):
    if f[-3:] == 'png':
        cmd = ("mv "+args.dir+f+" "+args.dir+"%05d.png") %(cnt)
        print(cmd)
        os.system(cmd)
        input
        cnt+=1
