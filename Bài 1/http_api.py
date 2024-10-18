import requests
import json

#Cách 1
def send_data_urlencoded(field1_value, field2_value):
    url = f"https://api.thingspeak.com/update"
    params = {
        'api_key': 'T7H40F0X82VGW7L5',
        'field1': field1_value,
        'field2': field2_value
    }
    response = requests.get(url, params=params)
    print(f"Response from urlencoded request: {response.json()}")

#Cách 2
def send_data_json(field1_value, field2_value):
    url = "https://api.thingspeak.com/update?api_key=T7H40F0X82VGW7L5"
    json_data = {
        "field1": field1_value,
        "field2": field2_value
    }
    response = requests.get(url, json=json_data)
    print(f"Response from JSON request: {response.json()}")


# Lấy dữ liệu từ Thingspeak:
def get_data_from_thingspeak():
    url = "https://api.thingspeak.com/channels/1529099/feeds.json"
    params = {'results': 2}  
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        for feed in data['feeds']:
            field1 = feed.get('field1')
            field2 = feed.get('field2')
        print(f"Temp (field1): {field1}, Humidity (field2): {field2}")
    else:
        print(f"Failed to fetch data, status code: {response.status_code}")

#Chạy cách 1:
send_data_urlencoded(20, 33)
#Chạy cách 2:
#send_data_json(21, 34)
#Lấy dữ liệu từ Thingspeak:
get_data_from_thingspeak()
