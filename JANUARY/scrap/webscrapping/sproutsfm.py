import requests
import pandas as pd

cookie= "_gcl_au=1.1.1870522609.1706678526; _gid=GA1.2.2143034726.1706678528; BVBRANDID=44bd90f1-c5b6-4f2a-b533-a2aa621c15aa; _fbp=fb.1.1706678528061.2114288924; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; loyaltyID=null; ajs_anonymous_id=7b482cc6-9dd7-4f91-806b-2206e1d21a77; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; ajs_anonymous_id=7b482cc6-9dd7-4f91-806b-2206e1d21a77; __stripe_mid=69b2421c-f664-47b0-8ada-3194ed0b62d7f36b12; __cf_bm=1SvrZlzIZng1lA5juA_SSPvoif8YBq5pYlBtf9w5o4k-1706783104-1-AeLniKSVwWT0Ky9mst82+lQ1sp2BV9IpzCJgrsSWxLgvDSzvCCBrdIgIa5jB/EOfqiek019XBDDcrA0hKAD/20Q=; __stripe_sid=d46c4a9c-4fb8-4263-9962-b70d6f14c33c1f35e1; BVBRANDSID=1fead0d2-24df-401b-8add-ae9e3be5a166; _gat_UA-47434162-1=1; dotcomSearchId=020d07f7-2033-470a-a05a-b9fad347b9d9; session-sprouts=.eJwdjsuOgjAARf-lazOBzviAncFHytASECmwIQgltBZUCiqdzL8PmcXdnNzknB-Q1z1TDbDrQiq2APmd9W3RsW4A9tCPM1FMKX7r8uF2ZR2wAZvc5nIsuc9ddNbIJNy1PmZoljCe5ukSyudFWvfMQSvUhm0KAxNHGfeiYIkhHsgubLBjLLE-SI-615TGIosagUUwEY4U6mKdJW5d0ID7AhlEb99E7F-Ev3hKw6Ggy39XAuUViftY0bfynDmqtUZGzWeVYO534VTRs0KtbKq5A0fli4j009-dNU6Mj9P8P6wDdnGck_f9iHtZ1A-92Y7-0diWb0iTQuwtZzpOG7AAo2J9zitgw6-1Ya5MY_X7B3eyakE.GJ0EEw.8n2mDMyKmuNh3_TLKJYw1fRs29s; _ga=GA1.2.1479835951.1706678528; _uetsid=b0217dd0bff811ee8ce8dd73f2fe6b07; _uetvid=b021a2c0bff811ee97982b12ce0f9533; _ga_LPZ816BHL5=GS1.1.1706783106.3.1.1706783380.3.0.0; _dd_s=rum=0&expire=1706784280593"

HEADERS={
    

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie   
    
    
}


# user_input=input("enter the items to search:")
# limit=int(input("enter the limit:"))



# URL=f"https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit={limit}&offset=0&search_provider=ic&search_term={user_input}&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false"


URL= "https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=60&offset=0&search_provider=ic&search_term=apple&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false"
responses=requests.get(URL,headers=HEADERS)
data =responses.json()


# for i in range(0,len(data['items'])):
#     print(f"name:{data['items'][i]['name']},price:{data['items'][i]['base_price']}")







# print(data)
# print(type(data))
# print(data.keys())


# print(data['items],name sale_price, sale_quantity,product_type)
# print(type(data['items'].keys()))




# for i in range(len(data)):
#     print(data['items'][i]['name']) ,print(data['items'][i]['base_price'])   




# for i in range(len(data)):
#     if name== "banana":
#         print(data['items'][i]['name'])  

