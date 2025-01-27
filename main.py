from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/products/aula-f3287-wired-tkl-rainbow-mechanical-gaming-keyboard-80-compact-tenkeyless-87-keys-layout-wtactile-blue-switches-white-grey-mixed-color-keycaps-programmable-macro-keys-i318797768-s1455591704.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Amechanical%252Bkeyboard%253Bnid%253A318797768%253Bsrc%253ALazadaMainSrp%253Brn%253Ad295d9d3b2fcd5272791ac5397a8ad5c%253Bregion%253Abd%253Bsku%253A318797768_BD%253Bprice%253A2549%253Bclient%253Adesktop%253Bsupplier_id%253A700508496048%253Bbiz_source%253Ah5_pdp%253Bslot%253A4%253Butlog_bucket_id%253A470687%253Basc_category_id%253A7847%253Bitem_id%253A318797768%253Bsku_id%253A1455591704%253Bshop_id%253A162836%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Chattogram&price=2549&priceCompare=skuId%3A1455591704%3Bsource%3Alazada-search-voucher%3Bsn%3Ad295d9d3b2fcd5272791ac5397a8ad5c%3BoriginPrice%3A254900%3BdisplayPrice%3A254900%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1737978825721&ratingscore=4.785714285714286&request_id=d295d9d3b2fcd5272791ac5397a8ad5c&review=14&sale=73&search=1&source=search&spm=a2a0e.searchlist.list.4&stock=1')
title = driver.find_element(By.CLASS_NAME,'pdp-mod-product-badge-title').text
print("Title of the Product: "+ title)
price = driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/span').text
print("Price of the Product: "+ price)
num_rating = driver.find_element(By.XPATH,'//*[@id="module_product_review_star_1"]/div/a').text
print("Number of Reviews: "+ num_rating)
time.sleep(5)
driver.quit()
