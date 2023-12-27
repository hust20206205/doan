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

contents =  os.path.join(git_folder, 'baocao/contents')
main =  os.path.join(git_folder, 'baocao/main.tex') 

MyFormat.latex_main(main)
# [MyFormat.latex_contents(i) for i in  glob.glob(os.path.join(
    # contents, f'**/*.tex'), recursive=True)]

MyView.CloseTab()
MyView.Target(2)
MyView.CloseTerminal()
MyView.CloseScrollBar()
# MyView.OpenLatex()
