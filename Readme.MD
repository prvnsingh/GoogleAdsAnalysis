Google Ads Analysis

- Scraping Google Ads for a webpage
 
- Extracting important feature of a Google Ad

Part 1: SeleniumAdScrapper.py -  Script uses Selenium (to scrape website that uses JS to render) and save the ads of the page in the directory "image". Initially hard coded url is "speedtest.net". Please change the URL as per your choice.

Part 2: Collab notebook for OCR and feature extraction of the google Ads (image).
https://colab.research.google.com/drive/15Ms3yeFxqfVdVPJ-zzXtmF_S9msMGVGJ?usp=sharing

Add/upload the image folder to the current session of the collab. 

Run the notebook (There might be prompts(press y/n) while installing libraries). It will loop through all the Ads’ images and do OpenCV easyOCR to find the dominant texts and their location. All the information is saved in the csv.

The last cell tries to extract feature of one ad using SIFT Algo (Scale Invariant Feature Transform).

Refresh the directory of Collab after running the notebook. A data.csv is created containing information of Ads. Column 1 shows the text extracted in an Ad and has the image of that text in pixel matrix.


Steps to follow:
- Ubuntu Env:
    1) install python
    2) install firefox
    3) pip install -r requirement.txt
    4) run script SeleniumAdScrapper.py 
    5) upload the images saved (in image folder saved in saved by previous script) on the collab env
    6) run the collab notebook
