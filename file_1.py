from flask import Flask, request

app=Flask(__name__)

#it is a method to check request type


@app.route('/profile/post')
def index():
    return 'The resquest type is %s' %request.method

if __name__=='__main__':
    app.run(debug=True);
