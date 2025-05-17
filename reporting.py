{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65a4c3e1-f570-44b1-a178-8502e3bc3306",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template_string, jsonify\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# This will store the latest report data (in memory for now)\n",
    "report_data = {}\n",
    "\n",
    "@app.route(\"/update-report\", methods=[\"POST\"])\n",
    "def update_report():\n",
    "    global report_data\n",
    "    report_data = request.json\n",
    "    return jsonify({\"status\": \"received\", \"message\": \"Report updated successfully\"})\n",
    "\n",
    "@app.route(\"/report\")\n",
    "def show_report():\n",
    "    if not report_data:\n",
    "        return \"<h2>No report submitted yet.</h2>\"\n",
    "    \n",
    "    # HTML rendering logic\n",
    "    html = f\"<h1>{report_data.get('title', 'Untitled Report')}</h1>\"\n",
    "    \n",
    "    if \"summary\" in report_data:\n",
    "        html += f\"<h2>Summary</h2><p>{report_data['summary']}</p>\"\n",
    "\n",
    "    if \"table\" in report_data:\n",
    "        html += \"<h2>Data Table</h2><table border='1'><tr><th>Metric</th><th>Value</th></tr>\"\n",
    "        for row in report_data[\"table\"]:\n",
    "            html += f\"<tr><td>{row['Metric']}</td><td>{row['Value']}</td></tr>\"\n",
    "        html += \"</table>\"\n",
    "\n",
    "    if \"recommendation\" in report_data:\n",
    "        html += f\"<h2>Recommendation</h2><p>{report_data['recommendation']}</p>\"\n",
    "\n",
    "    return html\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c19f03f7-0c4b-47b0-9086-394eb6b84e35",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
