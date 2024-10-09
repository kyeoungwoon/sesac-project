from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def github_webhook():
    if request.method == 'POST':
        data = request.json
        action = data.get('action')
        pull_request = data.get('pull_request')

        # PR이 생성되거나 다시 열렸을 때
        if action in ['opened', 'reopened']:
            pr_title = pull_request.get('title')
            pr_user = pull_request.get('user').get('login')
            pr_url = pull_request.get('html_url')

            # 여기에서 원하는 처리(예: 알림 전송) 수행
            print(f'📢 새로운 Pull Request 발생!\n제목: {pr_title}\n작성자: {pr_user}\nURL: {pr_url}')

        return jsonify({'status': 'Webhook received'}), 200
    else:
        return jsonify({'status': 'Method not allowed'}), 405

@app.route('/', methods=['GET'])
def greeting():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=8080, debug=True)