from flask import Flask, request, jsonify
import os

app = Flask(__name__)
report_data = {}

@app.route("/update-report", methods=["POST"])
def update_report():
    global report_data
    report_data = request.json
    return jsonify({"status": "received", "message": "Report updated successfully"})

@app.route("/report")
def show_report():
    if not report_data:
        return "<h2>No report submitted yet.</h2>"

    html = f"<h1>{report_data.get('title', 'Untitled Report')}</h1>"

    if "summary" in report_data:
        html += f"<h2>Summary</h2><p>{report_data['summary']}</p>"

    if "table" in report_data:
        html += "<h2>Data Table</h2><table border='1'><tr><th>Metric</th><th>Value</th></tr>"
        for row in report_data["table"]:
            html += f"<tr><td>{row['Metric']}</td><td>{row['Value']}</td></tr>"
        html += "</table>"

    if "recommendation" in report_data:
        html += f"<h2>Recommendation</h2><p>{report_data['recommendation']}</p>"

    return html

@app.route("/")
def index():
    return "<h2>Welcome to the Reporting API</h2><p>To view your latest report, visit <a href='/report'>/report</a></p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
