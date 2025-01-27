from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--disable-application-cache")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.daraz.com.bd/products/12-i492290190-s2378777329.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253A%253Bnid%253A492290190%253Bsrc%253ALazadaMainSrp%253Brn%253Af18c4e5997bca160a928ea322f850f08%253Bregion%253Abd%253Bsku%253A492290190_BD%253Bprice%253A259%253Bclient%253Adesktop%253Bsupplier_id%253A700518639803%253Bbiz_source%253Ahp_categories%253Bslot%253A19%253Butlog_bucket_id%253A470687%253Basc_category_id%253A20000420%253Bitem_id%253A492290190%253Bsku_id%253A2378777329%253Bshop_id%253A261382%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Dhaka&price=259&priceCompare=skuId%3A2378777329%3Bsource%3Alazada-search-voucher%3Bsn%3Af18c4e5997bca160a928ea322f850f08%3BoriginPrice%3A25900%3BdisplayPrice%3A25900%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1737995135273&ratingscore=&request_id=f18c4e5997bca160a928ea322f850f08&review=&sale=0&search=1&source=search&spm=a2a0e.searchlistcategory.list.19&stock=1')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

title = driver.find_element(By.CLASS_NAME,'pdp-mod-product-badge-title').text
print("\nTitle of the Product: "+ title)

price = driver.find_element(By.CSS_SELECTOR,'.notranslate.pdp-price.pdp-price_type_normal.pdp-price_color_orange.pdp-price_size_xl').text
print("\nPrice of the Product: "+ price)

details = driver.find_element(By.CSS_SELECTOR,'.html-content.pdp-product-highlights').text
print("\nDetails of the Product: "+ details)

rating = driver.find_element(By.CLASS_NAME,'score-average').text
print("\nRating: "+ rating)

num_review_string = driver.find_element(By.CSS_SELECTOR,'.pdp-link.pdp-link_size_s.pdp-link_theme_blue.pdp-review-summary__link').text
# print(type(num_rating))

num_review = re.search(r'\d+', num_review_string)
print("\nNumber of Reviews: ", num_review.group())

reviews = driver.find_elements(By.CLASS_NAME,'content')
print("\nList of All the Reviews ")

for i in range(len(reviews)):
    if(i == 0):
        continue
    print(f"\n Review {i}: " +reviews[i].text)

time.sleep(200)
driver.quit()