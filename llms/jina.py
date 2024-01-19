import http.client
import json
import os
from .llm_base import LLM_Base


class Jina(LLM_Base):

    def __init__(self) -> None:
        super().__init__()
        self.YOUR_GENERATED_SECRET = os.getenv('JINA_KEY')
        self.IMG = os.getenv('IMG')

    def call_llm(self, local_image_path, output_json_path):
        data = {
            "data": [
                {"image": self.image_to_data_uri(local_image_path),
                 "features": []},
            ]
        }

        headers = {
            "x-api-key": f"token {self.YOUR_GENERATED_SECRET}",
            "content-type": "application/json",
        }

        connection = http.client.HTTPSConnection("api.scenex.jina.ai")
        connection.request("POST", "/v1/describe", json.dumps(data), headers)
        response = connection.getresponse()

        # print(response.status, response.reason)
        response_data = response.read().decode("utf-8")
        with open(output_json_path, 'w') as fp:
            fp.write(response_data)

        connection.close()
