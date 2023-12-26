import os
from modules.MyGit import MyGit
# from modules.MyFormat import MyFormat
from modules.MyView import MyView

message = "VuVanNghia20206205"

git_folder =  os.path.join(os.getcwd(), '../../../')

MyGit.chdir(git_folder)
MyGit.add()
MyGit.commit(message)

# contents =  os.path.join(os.getcwd(), '../../../baocao/contents')
# main =  os.path.join(os.getcwd(), '../../../baocao/main.tex')
# init_path =  os.path.join(os.getcwd(), '../../../baocao/contents/start/init.sty')
# workspace_path = os.path.join(os.getcwd(), '../../report.code-workspace')
# gitignore_path = os.path.join(git_path, ".gitignore") 

# MyFormat.latex(contents)
# MyFormat.latex(main)
# MyFormat.markdown(git_path)
# MyFormat.basic(gitignore_path)
# MyFormat.basic(init_path)
# MyFormat.workspace(workspace_path)

MyView.CloseTab()
MyView.Target(2)
MyView.CloseTerminal()
MyView.CloseScrollBar()
MyView.OpenLatex()
