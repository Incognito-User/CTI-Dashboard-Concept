from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

def load_data():
    return pd.read_csv("data/Enriched_Test.csv")

@app.route("/")
def dashboard():
    df = load_data()

    # Convert dataframe to list of dicts for the HTML table
    records = df.to_dict(orient="records")

    # Example Plotly chart
    fig = px.scatter(
        df,
        x="EPSS_Score",
        y="Exploitability_Score",
        color="CVSS_Severity",
        hover_name="CVE_ID",
        title="EPSS vs Exploitability Score"
    )

    graph_html = fig.to_html(full_html=False)

    return render_template("dashboard.html", graph_html=graph_html, records=records)
