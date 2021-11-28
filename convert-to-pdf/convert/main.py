from services.downloader import download_pages
from services.rangeDownloader import rangeDownloader
from services.counter import counter
from services.converter import converter

# downloads specific pages
download_pages([45, 67])
# downloads pages in range
rangeDownloader(20, 22)
# converts to pdf
converter()
print(f"Downloaded Files: {counter()}")
