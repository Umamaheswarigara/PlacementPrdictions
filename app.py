
from flask import Flask, render_template, request
from flask import redirect
from flask import session
import os

from matplotlib import pyplot as plt
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
import io
import base64


UPLOAD_FOLDER = "uploads"
app = Flask(__name__)
app.secret_key='placement_prediction'

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if file.filename=="":
            return "NO File Selected"
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        # Save uploaded file
        file.save(file_path)
        session["dataset"]= filename
        return redirect("/summary")



    return render_template("upload.html")
@app.route("/summary")
def summary():
    filename = session.get("dataset")
    if filename is None :
        return redirect("/upload")
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_csv(filepath)
    return render_template(
        "summary.html",
        filename=filename,
        rows=df.shape[0],columns=df.shape[1],
        preview=df.head(10).to_html(classes="table,table-bordered",index=False),
         cat_cols = df.select_dtypes(exclude=np.number).columns.tolist(),


    )

    return render_template("summary.html")
@app.route("/visulazation")
def eda():
    filename = session.get("dataset")
    if filename is None :
        return redirect("/upload")
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_csv(filepath)
    plt.figure(figsize=(6,4))
    df["branch"].value_counts().plot(kind="bar")
    plt.title("Branch wise Students Count")
    buf=io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    bar_graph = base64.b64encode(buf.read()).decode("utf-8")

    plt.figure(figsize=(8, 5))
    plt.hist(df["age"], bins=10, edgecolor="black")
    plt.title("Age distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    hist_graph = base64.b64encode(buf.read()).decode("utf-8")

    plt.figure(figsize=(6, 4))
    plt.boxplot(df["age"])
    plt.title("Box Plot of Age")
    plt.ylabel("Age")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    box_plot = base64.b64encode(buf.read()).decode("utf-8")

    plt.close()
    buf.close()

    return render_template("visulization.html",bar_graph=bar_graph,hist_graph=hist_graph,box_plot=box_plot)

if __name__ == "__main__":
    app.run(debug=True)