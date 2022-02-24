import json
import requests
from scrap import Scrap


path = 'C:\\ChromeDriver\\chromedriver.exe'
scrap = Scrap(path)
thomann_website = "https://www.thomann.de/fr/index.html"
scrap.go_to_web_site(thomann_website)
scrap.close_cookie('/html/body/div[1]/div/div/div/div[2]/div[2]/button[1]')
scrap.sleep(2)
scrap.click_element('/html/body/div[3]/div/div[1]/div[1]/div[2]/div/div/ul/div/li[1]')
scrap.scroll_to_element('//*[@id="topseller"]/div/div[2]/div/div[2]/a')
scrap.click_element('//*[@id="topseller"]/div/div[2]/div/div[2]/a')

liste_nom = scrap.get_list_info('//*[@class="fx-ranked-product__title fx-text"]')
liste_prix = scrap.get_list_info('//*[@class="fx-typography-price-primary                                     fx-price-group__primary fx-ranked-product__price-primary"]')
liste_nbr_ventes = scrap.get_list_info('//*[@class="fx-rating-stars"]')

guitares = []
for i in range(len(liste_nom)):
    guitare_info = {}
    guitare_info['nom'] = liste_nom[i].text
    guitare_info['prix'] = liste_prix[i].text
    guitare_info['nbr_ventes'] = liste_nbr_ventes[i].text
    guitares.append(guitare_info)

scrap.sleep(3)
scrap.close_browser()

df = scrap.to_dataFrame(guitares,['nom', 'prix', 'nbr_ventes'])
df_json_dict = json.loads(df.to_json(orient = 'records'))
print(df_json_dict)

for i in range(len(df_json_dict)):
    requests.post('http://127.0.0.1:1234/guitares', json=df_json_dict[i])





