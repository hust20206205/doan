import os
import glob


def TimKiem(root_dir, ext):
 return glob.glob(os.path.join(
 root_dir, f'**/*{ext}'), recursive=True)


folder = os.path.join(os.getcwd(), "../../")
folder =   r"C:\Users\vvn20206205\Desktop\doan"
print( folder)
files = TimKiem(folder, '.srt')
files = TimKiem(folder, '.tex')
files = TimKiem(folder, '.md')
files = TimKiem(folder, '.py')
for f in files:
    print(f)


 