from flask import render_template, request, flash, redirect, url_for,  jsonify, Blueprint

from github import Github

git_bot = Github("99kies", "xxxxxxx")

api_v1 = Blueprint('api_v1', __name__)

repo = git_bot.get_repo("SUIBE-Blockchain/IssueStore")

@api_v1.route('/issuestore', methods=["POST", "GET"])
def issue_store():
    title = request.values.get('title')
    body = request.values.get('body')
    labels = request.values.get('labels')
    money = request.values.get('money')
    if title and body:
        if money is None:
            return jsonify({
                "result": "You need give some money.",
                "code": "201",
            })

        body = body + "<br><br><strong>赏金：￥" + money+ "</strong>"
        if labels:
            repo.create_issue(title=title, body=body, labels=[labels, ])
            return jsonify({
                "result": "Success Created.",
                "title": title,
                "body": body,
                "labels": labels,
                "code": "200"
            })
        else:
            repo.create_issue(title=title, body=body, labels=["development", ])
            return jsonify({
                "result": "Success Created.",
                "title": title,
                "body": body,
                "labels": labels,
                "code": "200"
            })
    return jsonify({
        "result": "Please post title and body.",
        "code": "201"
    })

    # for repo in g.get