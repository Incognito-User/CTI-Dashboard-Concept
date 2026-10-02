from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def load_data():
    df = pd.read_csv("data/enriched_test4.csv")
    return df

@app.route("/")
def dashboard():
    df = load_data()
    records = df.to_dict(orient="records")
    return render_template("dashboard.html", records=records)

if __name__ == "__main__":
    app.run(debug=True)
