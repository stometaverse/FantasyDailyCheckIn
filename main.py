import os
import httpx
import requests
import json

AUTH_TOKEN_COOKIE = ""
PAYLOAD_FOR_AUTH_TOKEN = {
    "user": {
        "id": "did:privy:placeholder",
        "createdAt": "2024-03-23T04:53:02.000Z",
        "linkedAccounts": [
            {
                "address": "placeholder",
                "type": "wallet",
                "verifiedAt": "2024-03-23T04:53:05.000Z",
                "chainType": "ethereum",
                "chainId": "eip155:1",
                "walletClient": "privy",
                "walletClientType": "privy",
                "connectorType": "embedded",
                "recoveryMethod": "privy"
            },
            {
                "subject": "placeholder",
                "username": "placeholder",
                "name": "placeholder",
                "type": "twitter_oauth",
                "profilePictureUrl": "placeholder",
                "verifiedAt": "2024-03-23T04:53:02.000Z"
            }
        ],
        "wallet": {
            "address": "placeholder",
            "chainType": "ethereum",
            "chainId": "eip155:1",
            "walletClient": "privy",
            "walletClientType": "privy",
            "connectorType": "embedded"
        },
        "twitter": {
            "subject": "placeholder",
            "username": "placeholder",
            "name": "placeholder",
            "profilePictureUrl": "placeholder"
        },
        "mfaMethods": [],
        "hasAcceptedTerms": True
    }
}

PAYLOAD_FOR_DAILY_QUEST = {
    "queryName": "GET_PLAYER_DAILY_QUEST_HISTORY",
    "variables": {
        "id": "placeholder_wallet_address"
    }
}
class AuthClient:
    def __init__(self):


    def retrieve_auth_token(self):
        url = "https://www.fantasy.top/api/auth/privy"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Cookie": AUTH_TOKEN_COOKIE,
            "Origin": "https://www.fantasy.top",
            "Priority": "u=1, i",
            "Referer": "https://www.fantasy.top/onboarding/home",
            "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }

        with httpx.Client(http2=True) as client:
            response = client.post(url, headers=headers, json=PAYLOAD_FOR_AUTH_TOKEN)

        if response.status_code == 200:
            print("Retrieving token successfully")
        else:
            print("Failed to retrieve token:", response.text)
        return response.json().get("token")

class DailyCheckinService:
    def __init__(self):
        self.authClient = AuthClient()
        self.auth_token = self.authClient.retrieve_auth_token()
        self.url = "https://www.fantasy.top/api/daily-quest"
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": f"Bearer {self.auth_token}",
            "Content-Length": "110",
            "Content-Type": "application/json",
            "Cookie": AUTH_TOKEN_COOKIE,
            "Origin": "https://www.fantasy.top",
            "Priority": "u=1, i",
            "Referer": "https://www.fantasy.top/rewards",
            "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"macOS\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }

    def dailyCheckin(self):

        response = requests.post(self.url, headers=self.headers, data=json.dumps(PAYLOAD_FOR_DAILY_QUEST))
        print("Status Code:", response.status_code)
        if response.status_code != 200:
            print("Error:", response.text)
        else:
            print("Response JSON:", response.json())

if __name__ == '__main__':
    service = DailyCheckinService()
    service.dailyCheckin()
