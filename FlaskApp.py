from flask import Flask, render_template
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Load the cleaned data
df = pd.read_csv('cleaned_amazon_products.csv')

# Define the home route
@app.route('/')
def index():
    # Render the data as an HTML table
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

# Output: A Flask web application displaying the cleaned data in a table format

