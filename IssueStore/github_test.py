from github import Github

g = Github("99kies", "xxxxx")

repo = g.get_repo("99Kies/a_pri")
for i in repo.get_issues():
    print(i)

# repo.create_issue("This is a test issue")
repo.create_issue(title="This   aweg", body="我需要你做xxxx<h1>hello</h1>",labels=["bug","b"])

# for repo in g.get_user().get_repos():
#     print(repo)