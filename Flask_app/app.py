from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the data
def load_data(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# File path to your Excel file
file_path = r"C:\Users\rodri\OneDrive\Documents\School - ULMaS\Industry Project - Yozu\data\network 8-10-24 CLEAN.xlsx"
data = load_data(file_path)

@app.route("/")
def index():
    # Render the main page with the data
    if data is not None:
        summary = data.describe().to_html(classes="table table-striped")
        return render_template("index.html", tables=[summary], titles=["Summary Statistics"])
    else:
        return "Error loading data."

@app.route("/filter", methods=["POST"])
def filter_data():
    # Handle filtering based on user input
    road_type = request.form.get("road_type")
    if road_type and "Road Type" in data.columns:
        filtered_data = data[data["Road Type"] == road_type]
        filtered_table = filtered_data.to_html(classes="table table-striped")
        return render_template("index.html", tables=[filtered_table], titles=["Filtered Data"])
    else:
        return render_template("index.html", tables=["No data available"], titles=["Error"])

if __name__ == "__main__":
    app.run(debug=True)
