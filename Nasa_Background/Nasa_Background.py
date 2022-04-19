import ctypes
import requests
from datetime import date
from PIL import Image, ImageFont, ImageDraw


image_path = ""
user = ctypes.windll.user32
screen_resolution = user.GetSystemMetrics(0), user.GetSystemMetrics(1)
SPI_SETDESKWALLPAPER = 0x0014
SPIF_UPDATEINIFILE = 0x0001
SPIF_SENDWININICHANGE = 0x0002


def draw_text(description):
    draw_list = description.split(".")
    draw_list = draw_list[::-1]
    font = ImageFont.truetype("arial.ttf", 15)
    image = Image.open("bg.png")
    draw_image = ImageDraw.Draw(image)
    y = screen_resolution[1] - 35 # Position text just above task bar
    line_spacing = 25
    for sentence in draw_list:
        sentence += "."
        draw_image.text((20,y), sentence.lstrip(), font=font)
        y -= line_spacing
    image.save("bg.png")


def get_nasa_background():
    today = date.today()
    base_url = ""
    params_dict = {'date': today}
    response = requests.get(base_url, params=params_dict)

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
        image = image.save("bg.png")
        draw_text(image_description)
        ctypes.windll.user32.SystemParametersInfoW.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint]
        ctypes.windll.user32.SystemParametersInfoW.restype = ctypes.wintypes.BOOL
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)

    else:
        print("Connection error")


if __name__ == "__main__":
    get_nasa_background()
