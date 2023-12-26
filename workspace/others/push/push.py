import os
import glob
from modules.MyGit import MyGit
from modules.MyFormat import MyFormat
from modules.MyView import MyView

message = "VuVanNghia20206205"

git_folder = os.path.join(os.getcwd(), '../../../')

MyGit.chdir(git_folder)
MyGit.add()
MyGit.commit(message)

workspace_path = glob.glob(os.path.join(
    git_folder, f'**/*.code-workspace'), recursive=True)
gitignore_path = glob.glob(os.path.join(
    git_folder, f'**/*.gitignore'), recursive=True)
start_path = glob.glob(os.path.join(
    git_folder, f'**/*.sty'), recursive=True)

[MyFormat.space(i) for i in workspace_path]
[MyFormat.space(i) for i in gitignore_path]
[MyFormat.space(i) for i in start_path]

contents =  os.path.join(os.getcwd(), '../../../baocao/contents')
print("🐍 File: push/push.py | Line: 27 | undefined ~ contents",contents)
main =  os.path.join(os.getcwd(), '../../../baocao/main.tex') 
print("🐍 File: push/push.py | Line: 29 | undefined ~ main",main)


# MyFormat.latex(contents)
# MyFormat.latex(main) 

MyView.CloseTab()
MyView.Target(2)
# MyView.CloseTerminal()
MyView.CloseScrollBar()
# MyView.OpenLatex()
