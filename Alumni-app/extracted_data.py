import time
import pickle
import requests
import httpx
import asyncio


file_name = "alumnis.json"

with open(file_name, "rb") as file:
    alumnis = pickle.load(file)


print(len(alumnis))


async def async_make_post_request(url, data):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=data)
            response.raise_for_status()
            return response
        except httpx.HTTPError as e:
            print("HTTP error:", e)
            return None


api_url = "http://localhost:5000/api/v1/alumni"


async def main():

    tasks = []

    i = 0
    for alumni in alumnis:
        # i += 1
        # if (i == 2):
        #     break
        data = {"name": alumni['name'], "about": alumni['about'],
                "linkedinUrl": alumni['profile_url'], "imageUrl": alumni['image_url'], "university": "NIT Agartala"};
        tasks.append(async_make_post_request(api_url, data))

    responses = await asyncio.gather(*tasks)

    for i, response in enumerate(responses):
        if response:
            print(f"Response {i+1} status code: {response}", )
        else:
            print(f"Response {i+1} failed")


asyncio.run(main())