from abc import ABC
from dotenv import load_dotenv
import base64


class LLM_Base(ABC):
    load_dotenv()

    def image_to_data_uri(self, file_path):
        with open(file_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded_image}"
