import web
from Models import UserModel

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/register-post', 'RegisterPost',
    '/login', 'Login',
    '/login-authenticate', 'LoginAuthenticate',
    '/logout', 'Logout'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('session'), initializer={'user': None})
session_data = session.initializer


render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data['user']})


class Home:
    def GET(self):
        return render.Home()


class Register:
    def GET(self):
        return render.Register()


class RegisterPost:
    def POST(self):
        data = web.input()
        user_model = UserModel.UserModel()
        user_model.create_user(data)


class Login:
    def GET(self):
        return render.Login()


class LoginAuthenticate:
    def POST(self):
        data = web.input()
        user_model = UserModel.UserModel()
        valid_user = user_model.check_user(data)
        if valid_user:
            session_data['user'] = valid_user
            return valid_user
        else:
            return 'error'


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return 'success'


if __name__ == '__main__':
    app.run()
