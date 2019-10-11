from git import Repo
from sty import fg, bg, ef, rs

class GitHandler:

    def __init__(self,repo_dir):
        self.repo_dir = repo_dir
        self.repo = Repo(repo_dir)

    def get_branches(self):
        self.branches = self.repo.branches
        self.branch = self.repo.active_branch
        return self.branches

#    def set_branch(self):

    def display_branches(self):
        self.get_branches()

        print(fg.li_white+"Available branches")
        print(fg.da_white+"------------------------------------------------------")
        print(fg.li_white+"Current?  Branch name")
        print(fg.da_white+"------------------------------------------------------")
        for i in self.branches:
            curr = "          "
            if i == self.branch:
                curr = " *        "
            print(fg.da_red + curr+
                  fg.da_yellow + i)





#g = GitHandler('/Users/shayneoneill/quantify-ios/')
#g.display_branches()