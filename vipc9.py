import requests

def login_and_qiandao(username, password):
    # 创建一个会话以保持请求之间的Cookie
    session = requests.Session()

    # 第一步：登录
    login_url = "https://vipc9.com/wp-admin/admin-ajax.php"
    login_payload = {
        "action": "user_login",
        "username": username,
        "password": password
    }

    # 执行登录
    login_response = session.post(login_url, data=login_payload)

    # 检查登录是否成功
    if login_response.status_code == 200:
        print("登录成功!")
        print("登录后的Cookies:", session.cookies.get_dict())
    else:
        print("登录失败，状态码:", login_response.status_code)
        return

    # 第二步：执行“签到”操作
    qiandao_url = "https://vipc9.com/wp-admin/admin-ajax.php"
    qiandao_payload = {
        "action": "user_qiandao"
    }

    # 使用会话发送签到请求
    qiandao_response = session.post(qiandao_url, data=qiandao_payload)

    # 检查签到请求是否成功
    if qiandao_response.status_code == 200:
        print("签到成功!")
        print("响应内容:", qiandao_response.text)
    else:
        print("签到失败，状态码:", qiandao_response.status_code)

# 调用函数并传入用户名和密码
login_and_qiandao("your_username", "your_password")
