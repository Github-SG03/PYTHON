import requests # type: ignore
import csv

def fetch_data_from_api(api_url, output_csv):
    try:
        # Fetch data from the API3.10
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # Open the CSV file for writing
        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write headers (assuming data is a list of dictionaries)
            if data and isinstance(data, list):
                writer.writerow(data[0].keys())

                # Write data rows
                for row in data:
                    writer.writerow(row.values())

        print(f"Data successfully saved to {output_csv}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except Exception as e:
        print(f"Error writing to CSV: {e}")

if __name__ == "__main__":
    # Example usage
    api_url = "https://jsonplaceholder.typicode.com/posts"  # Replace with your API URL
    output_csv = "output.csv"  # Replace with your desired output file name
    fetch_data_from_api(api_url, output_csv)