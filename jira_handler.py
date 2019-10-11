from jira import JIRA
from jira.resources import Issue
import urllib3
from sty import fg, bg, ef, rs
import utils

class JiraWrap:



    def __init__(self, host, username, key):
        urllib3.disable_warnings()
        self.options = {'server': host, 'verify': False}
        self.jira = JIRA(options=self.options, basic_auth=(username, key))
        self.selected = []

    def set_query(self, query):
        self.query = query

    def retrieve_issues(self, start_at=0, max_results=150):
        self.issuelist = self.jira.search_issues(self.query, startAt=start_at, maxResults=max_results)
        return self.issuelist

    def show_issues(self):
        print(fg.da_white + "Filter: " + fg.li_green + self.query)

        issues = self.retrieve_issues()
        self.render_issues(issues)

    def render_issues(self, issues,selected=False):
        print(fg.white + "-" * 120)
        print(fg.li_white + "+ ID  KEY         STATUS      DESCRIPTION")
        print(fg.white + "-" * 120)
        counter = 0
        for i in issues:
            issue_color = fg.blue
            flag = "  "
            if str(i.fields.status) == "In Progress":
                issue_color = fg.red
            if str(i.key) in self.selected:
                flag = fg.li_red + "* "
            preamble = flag+ fg.li_yellow + "{:<4}".format(counter)
            if selected:
                preamble = "      "
            print(preamble +
                  fg.green + "{:12}".format(i.key) +
                  issue_color + "{:12}".format(str(i.fields.status)) +
                  fg.white + i.fields.summary)
            counter += 1
        print(fg.white + "-" * 120)

    def get_issue(self):

        utils.pretty_menu([
            {'key': 'O', 'data': 'key', 'desc': 'Toggle Issue with specific Key'},
            {'key': '', 'data':'0..99', 'desc': 'Toggle issue from above list'},
            {'key': 'F', 'data':'filter', 'desc': 'Specify new issue filter'},
            {'key': 'L', 'data': '', 'desc': 'Show current selected List'},
            {'key': 'Q', 'data':'', 'desc': 'Quit list'}
        ])
        r = input(fg.white + "Selection >" + fg.li_yellow)
        try:
            i = int(r)
            self.issue = self.issuelist[int(r)]
            return self.issue
        except:
            pass
        if r[0] == 'O':
            print (fg.red+"Attempting to retrieve {}".format(r[1:100]))
            try:
                self.issue = self.jira.issue(r[1:20])
                return self.issue
            except:
                pass
        if r[0] == 'F':
            self.set_query(r[1:1024])
            return "NewFilter"
        if r[0] == 'Q':
            return "Quit"
        if r[0] == 'L':
            self.show_list()
        return False

    def show_list(self):
        print(fg.da_white + "Filter: " + "Currently selected issues")
        issues = []
        for i in self.selected:
            issue = self.jira.issue(i)
            issues.append(issue)
        self.render_issues(issues,True)
        print("")

    def menu_loop(self):
        finished = False
        while not finished:
            j.show_issues()
            result = j.get_issue()
            #import ipdb; ipdb.set_trace()
            if isinstance(result,Issue):
                print(result)
                if str(result.key) in self.selected:
                    self.selected.remove(str(result.key))
                else:
                    self.selected.append(str(result.key))
            else:
                if 'Quit' == result: #yes this looks back to front, but issues overrides the equality operator
                    finished = True


#j.set_query('resolution = Unresolved AND "Epic Link" = JPT510-15 ORDER BY updated DESC')
#j.menu_loop()
