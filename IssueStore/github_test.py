from github import Github
from pprint import pprint

import time
g = Github("99kies", "xxxxxxxxxxxxxxx")
time.sleep(2)

# repo = git_bot.get_repo("SUIBE-Blockchain/IssueStore")
repo = g.get_repo("99Kies/a_pri")
issues_list = []
# issue_dict = {}
for i in repo.get_issues():
    issue_dict = {}
    # print(i.labels)
    # print(i.labels)
    # for label in i.labels:
    #     print(label.name)
    issue_dict['labels'] = [label.name for label in i.labels]
    # print(i.title)
    issue_dict['title'] = i.title
    issue_dict['body'] = i.body
    issue_dict['number'] = i.number
    issues_list.append(issue_dict)

pprint(issues_list)
# for i in issues_list:
#     print(i['labels'])

# repo.create_issue("This is a test issue")
# repo.create_issue(title="This   aweg", body="我需要你做xxxx<h1>hello</h1>",labels=["bug","b"])

# for repo in g.get_user().get_repos():
#     print(repo)