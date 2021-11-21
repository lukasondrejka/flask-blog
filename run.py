from app import app


if __name__ == '__main__':
    # app.run(debug=False)
    app.run(debug=True, use_reloader=True)  # development
