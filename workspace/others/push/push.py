import os
import glob
from modules.MyGit import MyGit
from modules.MyFormat import MyFormat
from modules.MyView import MyView

message = "VuVanNghia20206205"

git_folder =  os.path.join(os.getcwd(), '../../../')

MyGit.chdir(git_folder)
MyGit.add()
MyGit.commit(message)

workspace_path =   glob.glob(os.path.join(git_folder, f'**/*.code-workspace'), recursive=True)
gitignore_path =   glob.glob(os.path.join(git_folder, f'**/*.gitignore'), recursive=True)


MyFormat.space(gitignore_path)
MyFormat.space(workspace_path)

# contents =  os.path.join(os.getcwd(), '../../../baocao/contents')
# main =  os.path.join(os.getcwd(), '../../../baocao/main.tex')
# init_path =  os.path.join(os.getcwd(), '../../../baocao/contents/start/init.sty')


# MyFormat.latex(contents)
# MyFormat.latex(main)
# MyFormat.markdown(git_path)
# MyFormat.basic(init_path)

MyView.CloseTab()
MyView.Target(2)
MyView.CloseTerminal()
MyView.CloseScrollBar()
MyView.OpenLatex()
