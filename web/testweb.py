#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import render_template,url_for,jsonify,abort,request,Flask,make_response,redirect
from werkzeug import secure_filename


app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('home.html')


#get请求
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


#post请求
@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


#rest风格请求
@app.route('/signin/hello', methods=['GET'])
def hello():
    # 需要从request对象读取表单内容：
    return '<h3>test Hello rest</h3>'

#返回json
@app.route('/signin/json', methods=['GET'])
def json():
    # 需要从request对象读取表单内容：
    return jsonify({'test':'ssss','test1':123})

#报错页面
@app.route('/signin/abort', methods=['GET'])
def abort1():
    # 需要从request对象读取表单内容：
    abort(404)

#重新定义404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#上传页面(使用模板)
@app.route('/upload', methods=['GET'])
def upload_file():
    return render_template('file_upload.html')

#上传文件
@app.route('/upload', methods=['POST'])
def upload_file_do():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('E://pythonWorkspace/learn/pythonlearn/web/' + secure_filename(f.filename))
    return "<h1>上传成功</h1>"

#设置cookie
@app.route('/set_cookie')
def setCookie():
    resp = make_response(render_template('home.html'))
    resp.set_cookie('username', 'the username')
    return resp

#获取cookie
@app.route('/get_cookie')
def getCookie():
    username = request.cookies.get('username')
    return "<h1>"+username+"</h1>"

#重定向
@app.route('/test_redirect')
def testRedirect():
    return redirect('/signin/json')

if __name__ == '__main__':
    app.debug = True
    app.run(debug = True,host='0.0.0.0')