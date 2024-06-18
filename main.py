import requests
import csv

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

if __name__ == "__main__":
    page_id = "your_facebook_page_id"
    access_token = "your_facebook_access_token"
    data = fetch_facebook_page_data(page_id, access_token)
    if data:
        save_to_csv(data)
        print("Data saved to facebook_page_data.csv")
    else:
        print("Failed to fetch data")


