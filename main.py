from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import csv
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flash messages

# URLs to your hosted ToS and Privacy Policy
TOS_URL = "https://shivamkumar-09890.github.io/app-doc/tos.html"
PRIVACY_POLICY_URL = "https://shivamkumar-09890.github.io/app-doc/privacy-policy.html"

def fetch_facebook_page_data(page_id, access_token):
    url = f"https://graph.facebook.com/{page_id}?access_token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_to_csv(data, filename='facebook_page_data.csv'):
    # Extract the required fields
    fields = ['id', 'name', 'likes', 'followers_count','text']
    rows = []

    # Extract the values for each field
    row = [data.get(field, '') for field in fields]
    rows.append(row)

    # Write to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Writing the header
        csvwriter.writerow(fields)
        
        # Writing the data
        csvwriter.writerows(rows)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        page_id = request.form['page_id']
        access_token = request.form['access_token']
        data = fetch_facebook_page_data(page_id, access_token)
        if data:
            save_to_csv(data)
            flash('Data saved to facebook_page_data.csv', 'success')
        else:
            flash('Failed to fetch data', 'danger')
        return redirect(url_for('index'))
    return render_template('index.html', tos_url=TOS_URL, privacy_policy_url=PRIVACY_POLICY_URL)

if __name__ == '__main__':
    app.run(debug=True)
