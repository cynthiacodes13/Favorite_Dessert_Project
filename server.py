import os
from flask import Flask, render_template, request,session, flash, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "CCC"


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template('homepage.html')


@app.route("/show_image", methods=["GET","POST"])
def upload_file():
    """Upload image"""
    

    if request.method == "POST":
        f = request.files['image']
        f.save(os.path.join("image", f.filename))
        print(f.filename)

    return render_template("image_page.html", f = f.filename)






if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
