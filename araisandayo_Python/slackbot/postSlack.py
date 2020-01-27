import requests, json

WEB_HOOK_URL = "https://hooks.slack.com/services/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"
requests.post(WEB_HOOK_URL, data = json.dumps({
    'text': u'Notifycation From Python.',  #通知内容
    'username': u'Bakira-Tech-Python-Bot',  #ユーザー名
    'icon_emoji': u':smile_cat:',  #アイコン
    'link_names': 1,  #名前をリンク化
}))
