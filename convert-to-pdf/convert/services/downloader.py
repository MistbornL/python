import requests

img = []


def download_pages(pages):
    for page in pages:
        url = f"https://img.yumpu.com/54761731/{page}/900x900/7uhbctpd0.jpg?quality=100"
        r = requests.get(url)
        img.append(r.content)

        for pic in img:
            with open(f"{pages.index(page)}.jpeg", 'wb') as f:
                f.write(pic)
