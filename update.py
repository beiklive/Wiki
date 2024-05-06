from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Git 仓库路径
repo_path = '/path/to/your/git/repository'

@app.route('/pull', methods=['GET'])
def git_pull():
    try:
        # 执行 git pull 操作
        cmd = f'git -C {repo_path} pull'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            message = "Git pull successful"
            status = True
        else:
            message = f"Error during git pull:\n{result.stderr}"
            status = False
    except Exception as e:
        message = f"Error during git pull: {str(e)}"
        status = False

    # 返回 JSON 响应
    return jsonify({'status': status, 'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10666)
