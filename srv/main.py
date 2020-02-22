import os
import string
import random
from flask import Flask, request, abort, send_from_directory, url_for
from flask import current_app as app
from werkzeug.utils import secure_filename


def allowed_file(fn):
    return "." in fn and fn.rsplit(".", 1)[1].lower() in app.config["ALLOWED_FILES"]


def random_fn(
    size=app.config["FILENAME_LEN"], chars=string.ascii_lowercase + string.digits
):
    return "".join(random.choice(chars) for _ in range(size))


def verify(k):
    if k == os.environ.get("UPLOAD_KEY"):
        return True
    else:
        return False


@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        abort(404)

    key = request.form["key"]
    f = request.files["file"]

    if verify(key):
        if f and allowed_file(f.filename):
            fext = f.filename.rsplit(".", 1)[1].lower()
            fn = secure_filename(random_fn() + "." + fext)
            f.save(os.path.join(app.config["UPLOADS_DIR"], fn))
            return f"{app.config['HOST']}" + fn
        else:
            return "idk"

    else:
        return "your key is borked"
