import json
import base64
import time

import requests


def submit_post(url: str, data: dict):
    """
    Submit a POST request to the given URL with the given data.
    """
    return requests.post(url, data=json.dumps(data))


def save_encoded_image(b64_image: str, output_path: str):
    """
    Save the given image to the given output path.
    """
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))


if __name__ == '__main__':
    txt2img_url = 'http://127.0.0.1:7861/sdapi/v1/txt2img'
    prepend= str(time.time())
    with open("animals.txt", "rt") as handle:
        lines = handle.readlines()
#    lines = ["dog"]
    for line in lines:
        print(line)
        # 'styles': ['line drawing'],
        data = { 'width':1024, 'height': 768, 'num_inference_steps': 100,
                 'prompt':
                     f"""
                     show a anime bunny girl drinking coffee, wearing a red t-shirt that says 'horse' and reading a math book alone in a dirty dorm room with a square of tofu on the table
                     """}
        response = submit_post(txt2img_url, data)
        save_encoded_image(response.json()['images'][0], f"graphics/{prepend}-{line}.png")

