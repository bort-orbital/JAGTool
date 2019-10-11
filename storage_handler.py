import ruamel.yaml
import os
yaml = ruamel.yaml.YAML()

class Setup:
    def __init__(self):
        self.jira_username = ''
        self.jira_key = ''
        self.jira_host = ""
        self.current_issues = []
        self.development_branch = ""
        self.hotfix_branch = ""
        self.production_branch = ""
        self.current_branch = ""
        self.current_type = ""

yaml.register_class(Setup)

class StorageHandler:

    def __init__(self):
        self.__options = Setup()

        pass

    def check_init(self):
        if not os.path.exists(".JAGtool"):
            with open(".JAGtool","w") as f:
                yaml.dump([self.__options],f)
        with open(".JAGtool","r") as f:
            y = yaml.load(f)
            print (y[0])



    def setOptions(self,options):
        self.__options = options

    def getOptions(self):
        return self.__options




x = StorageHandler()
x.check_init()