import ctypes
import requests
import os
import re
from datetime import date
from PIL import Image, ImageFont, ImageDraw


def draw_description(image, description, screen_resolution):
    """Appends/draws text description to the wallpaper image.
    
    Args:
        image: PIL image object to draw description on.
        description: The text description, from the API.
        screen_resolution: user's screen resolution via
        user.GetSystemMetrics. Used to position text in
        correct y-coordinate.

    Returns:
        PIL image object with description drawn within bottom-left portion.
    """
    draw_list = re.split(r"(?<=\.) ", description)[::-1]
    font = ImageFont.truetype("arial.ttf", 15)
    draw_image = ImageDraw.Draw(image)
    y = screen_resolution[1] - 60 # Position text just above task bar
    line_spacing = 25
    for sentence in draw_list:
        draw_image.text((20,y), sentence.lstrip(), font=font)
        y -= line_spacing
    return image


def get_nasa_image(user):
    """Queries NASA's Photo of Day API to download latest image.

    Args:
        user: User's WinDLL object. Used to access user's screen resolution.

    Returns:
        Completed PIL image object, or None if error occurs.
    """
    base_url = "https://api.nasa.gov/planetary/apod?api_key="
    api_key = os.environ.get('NASA_API_KEY')
    params_dict = {'date': date.today()}
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

        screen_resolution = user.GetSystemMetrics(0), user.GetSystemMetrics(1)
        image = image.resize(screen_resolution)
        image = draw_description(image, image_description, screen_resolution)
        return image

    else:
        print("Connection error")


def main():
    """Script execution begins in main().

    Creates a directory for saving wallpapers if it doesn't already exist.
    Calls get_nasa_image() and updates Window's wallpaper to the returned 
    image.
    """
    wallpaper_dir = "wallpapers/"
    if not os.path.exists(wallpaper_dir):
        os.makedirs(wallpaper_dir)

    user = ctypes.windll.user32
    image = get_nasa_image(user)

    if image is None:
        return

    image_name = str(date.today()) + '.jpg'
    image.save(wallpaper_dir + image_name)

    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x0001
    SPIF_SENDWININICHANGE = 0x0002
    user.SystemParametersInfoW.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint]
    user.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(wallpaper_dir + image_name), SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)


if __name__ == "__main__":
    main()
