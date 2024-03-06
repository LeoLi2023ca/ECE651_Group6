from my_app import create_app
from my_app.account import account
from my_app.post import post

app = create_app()

app.register_blueprint(account)
app.register_blueprint(post)

if __name__ == '__main__':
    app.run(debug=True)