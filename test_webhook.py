
import requests

user_message = "can u tell me the conversion factor of 100 rs(india) in doller using current value use search tool as web "

url = "https://siddpatel.app.n8n.cloud/webhook-test/b88cc008-6b2b-457e-82fa-d1a4224fa2cb"

payload = {
    "message": user_message
}

try:
    response = requests.post(url, json=payload, timeout=60)

    print("Status Code:", response.status_code)
    print("Response Text:", repr(response.text))

    if response.status_code == 200 and response.text.strip():
        try:
            data = response.json()
            print("\nAI OUTPUT:")
            if isinstance(data, dict):
                print(data.get("output", data))
            elif isinstance(data, list):
                print(data[0].get("output", data[0]) if data else "Empty list")
            else:
                print(data)
        except ValueError:
            print("Response is plain text:", response.text)
    else:
        print("No AI response received from n8n.")

except requests.exceptions.RequestException as e:
    print("Request Error:", e)
