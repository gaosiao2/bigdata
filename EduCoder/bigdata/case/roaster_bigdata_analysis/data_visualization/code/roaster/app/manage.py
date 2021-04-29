from app import crate_app

app = crate_app('development')

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080)

