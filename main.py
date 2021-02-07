from website import create_app

app = create_app()

if __name__ == '__main__': # this condition prevents the website from running if main.py is imported
    app.run(debug=True) # allows the updates to website to automatically load to website; useful for development