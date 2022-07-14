import ctypes
import requests
import os
from datetime import date
from PIL import Image, ImageFont, ImageDraw


user = ctypes.windll.user32
screen_resolution = user.GetSystemMetrics(0), user.GetSystemMetrics(1)
SPI_SETDESKWALLPAPER = 0x0014
SPIF_UPDATEINIFILE = 0x0001
SPIF_SENDWININICHANGE = 0x0002


def draw_text(description):
    """Appends text description to the background image.
    
    Args:
        description: The text description, from the API, to be appended.
    """
    draw_list = description.split(".")
    draw_list = draw_list[::-1]
    font = ImageFont.truetype("arial.ttf", 15)
    image = Image.open("bg.jpg")
    draw_image = ImageDraw.Draw(image)
    y = screen_resolution[1] - 35 # Position text just above task bar
    line_spacing = 25
    for sentence in draw_list:
        sentence += "."
        draw_image.text((20,y), sentence.lstrip(), font=font)
        y -= line_spacing
    image.save("bg.jpg")


def get_nasa_background():
    """Queries NASA's Photo of Day API to download latest image."""
    today = date.today()
    base_url = "https://api.nasa.gov/planetary/apod?api_key="
    api_key = os.environ.get('NASA_API_KEY')
    params_dict = {'date': today}
    response = requests.get(base_url + api_key, params=params_dict)

    if response.status_code == 200:
        try:
            # Verify Photo of the Day is an actual image and not video
            data = response.json()
            image_url = data['hdurl']
            image_description = data['explanation']
            image = Image.open(requests.get(image_url, stream=True).raw)
        except:
            print("Photo of the day is not available today.")
            return

        # Resize the image, save, and set as background
        image = image.resize(screen_resolution)
        image = image.save("bg.jpg")
        draw_text(image_description)
        user.SystemParametersInfoW.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint]
        user.SystemParametersInfoW.restype = ctypes.wintypes.BOOL
        user.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath("bg.jpg"), SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)

    else:
        print("Connection error")


if __name__ == "__main__":
    get_nasa_background()
