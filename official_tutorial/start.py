import flaskr

if __name__ == '__main__':
    port = 5000
    url = '127.0.0.1'
    app = flaskr.create_app()
    app.run(host=url, port=port, debug=True, use_reloader=True)