import requests
from bs4 import BeautifulSoup

cookies = {
    '_pcid': '%7B%22browserId%22%3A%22lx21xtquy6tllmgo%22%7D',
    'usprivacy': '1---',
    'OneTrustWPCCPAGoogleOptOut': 'true',
    'omni_visit_id': 'billboard.1717605453465.15762aa0-ca9f-4ac2-826b-d74405946c6b',
    '_gcl_au': '1.1.1543521680.1717605454',
    'pmc_piano_reporting': '%7B%22entitlements%22%3A%22%22%2C%22user_type%22%3A%22ANONYMOUS%22%2C%22acct_id%22%3Anull%2C%22acct_type%22%3Anull%2C%22org_id%22%3Anull%2C%22org_name%22%3Anull%2C%22paywall_logged_in%22%3Afalse%7D',
    '__pat': '0',
    '_pctx': '%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXQF8g',
    '_parsely_session': '{%22sid%22:1%2C%22surl%22:%22https://www.billboard.com/c/music/music-news/%22%2C%22sref%22:%22https://www.google.com/%22%2C%22sts%22:1717605453829%2C%22slts%22:0}',
    '_parsely_visitor': '{%22id%22:%22pid=4e1405e5-3460-4e72-816a-016739c7369c%22%2C%22session_count%22:1%2C%22last_session_ts%22:1717605453829}',
    'AMP_TOKEN': '%24NOT_FOUND',
    '_gid': 'GA1.2.1084081258.1717605454',
    '_hjSession_2036991': 'eyJpZCI6IjEyNmJlNTViLTBiMWItNDc4Zi04MzE5LTI0MDUwZTdhZjBhZCIsImMiOjE3MTc2MDU0NTQxNDksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '__td_signed': 'true',
    '__td_blockEvents': 'false',
    'pmc_atlasmg_id': '467ca42a-d6ae-4de9-b452-cbed5ed47545',
    '_td_ssc_id': '01HZMM6M1FRWQS78NTNXAK9SD8',
    '__browsiSessionID': '842abeb3-2e0e-42f2-a856-0981447eda75&false&false&SEARCH&kz&desktop-4.25.21&false',
    '__browsiUID': '7d1b1ac4-ec1f-4f3c-8995-46411da75c48',
    '_lr_retry_request': 'true',
    '_lr_env_src_ats': 'false',
    'billboard_fonts_loaded': '1',
    '_lr_geo_location': 'KZ',
    '_cc_id': '3f4c227604aa1247f71334bf4e56aba4',
    'panoramaId_expiry': '1718210255960',
    'panoramaId': 'a7387dd6c9529ce2ef43d6ef6edd4945a702a1bdbc93bc698e41d70b92355529',
    'panoramaIdType': 'panoIndiv',
    '_au_1d': 'AU1D-0100-001717605457-OENMMAH7-V0JI',
    'TAPAD': '%7B%22id%22%3A%22e0e1eb5b-b23b-4ce2-abb4-099e677f6143%22%7D',
    '__qca': 'P0-599749289-1717605461169',
    '_ga_FVWZ0RM4DH': 'GS1.1.1717606045.1.0.1717606045.60.0.0',
    '_hjSessionUser_2036991': 'eyJpZCI6IjMwOWViZGY2LTBjN2ItNTE2OS04NjRiLWEzMmRjYmU1N2MyMSIsImNyZWF0ZWQiOjE3MTc2MDU0NTQxNDcsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga': 'GA1.2.558969231.1717605453',
    '__pvi': 'eyJpZCI6InYtMjAyNC0wNi0wNS0yMy0wMS0wOS00MTItRjZSd3NDc3NWcmpsSlNpVS01MDRiNzNjMGY1YTE4YTBiMTYwMjNmMDRmMzAxNDY4YSIsImRvbWFpbiI6Ii5iaWxsYm9hcmQuY29tIiwidGltZSI6MTcxNzYwNjg2OTQxMn0%3D',
    'xbc': '%7Bkpex%7DBnIdpzS3aa8aHAptq9RDSQ',
    '__tbc': '%7Bkpex%7DcqJsVdztcocBKNdqfNeC6yG6PpzlRPbtx0t3LEI_szgH9s8RDsZysP2oXvsO1sSr',
    '_gat_UA-76834886-1': '1',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Jun+05+2024+23%3A01%3A10+GMT%2B0600+(Kyrgyzstan+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=9dbeb4d8-50e8-4ca6-aef6-348aa3946ea8&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.billboard.com%2Fc%2Fmusic%2Fmusic-news%2F&groups=C0002%3A1%2CC0004%3A1%2CC0001%3A1%2CC0003%3A1',
    '_ga_DJBCNPKNBT': 'GS1.1.1717605453.1.1.1717606870.60.0.0',
    '_gat': '1',
    '_ga_FCQQWSJ01C': 'GS1.2.1717605454.1.1.1717606871.0.0.0',
    '_td': 'b69e3b58-9339-4c98-a414-43aa9f1a3cd5',
    '_awl': '2.1717606870.5-e31273dfb4ff98406af791d3dd0219de-6763652d6575726f70652d7765737431-0',
    '_gat_pianoTracker': '1',
    '__eoi': 'ID=e89dfc0516f5db6d:T=1717605456:RT=1717606873:S=AA-AfjbFZazhkpwWcbkRv-_WX0mf',
    '__gads': 'ID=4a8d301058768919:T=1717605456:RT=1717606873:S=ALNI_MZ6w5FE-7skRN2eZlOxeA9BM55AMQ',
    '__gpi': 'UID=00000e4b89246758:T=1717605456:RT=1717606873:S=ALNI_MakrE9RFyi2iYFQE_iKMV6Wav3ZlQ',
    'cto_bundle': 'VoOdQV9rT2glMkJJbjJ4ZzJPUGlvVHUlMkIxdUZGSGRLQU9Heng0R0diYiUyRlBPZkZ2b0NaRDZ5ZTBQT1FLQzhGaTl5S2NEc0Y0c3l4Nkw1dk0zZWpCNW9kRUpDc2ZCYzQ4V2dTTnElMkJPWGJxNzU1dldyJTJGb0ZXV2ZNc2RxdnB3Umg1dVZJWk9NN1ZvcGE2VnZuaHpCN3l3RHVHaWw5Z1I0aXBmNTVabDB0MkhrU2xvQnliJTJCUmVPdU9jTXdOaFJmM3VuVXZ6UCUyRkhzYkJiSWNrMiUyQjNzbkxZRkJNVkcyZUN5QSUzRCUzRA',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': '_pcid=%7B%22browserId%22%3A%22lx21xtquy6tllmgo%22%7D; usprivacy=1---; OneTrustWPCCPAGoogleOptOut=true; omni_visit_id=billboard.1717605453465.15762aa0-ca9f-4ac2-826b-d74405946c6b; _gcl_au=1.1.1543521680.1717605454; pmc_piano_reporting=%7B%22entitlements%22%3A%22%22%2C%22user_type%22%3A%22ANONYMOUS%22%2C%22acct_id%22%3Anull%2C%22acct_type%22%3Anull%2C%22org_id%22%3Anull%2C%22org_name%22%3Anull%2C%22paywall_logged_in%22%3Afalse%7D; __pat=0; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXQF8g; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.billboard.com/c/music/music-news/%22%2C%22sref%22:%22https://www.google.com/%22%2C%22sts%22:1717605453829%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=4e1405e5-3460-4e72-816a-016739c7369c%22%2C%22session_count%22:1%2C%22last_session_ts%22:1717605453829}; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1084081258.1717605454; _hjSession_2036991=eyJpZCI6IjEyNmJlNTViLTBiMWItNDc4Zi04MzE5LTI0MDUwZTdhZjBhZCIsImMiOjE3MTc2MDU0NTQxNDksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __td_signed=true; __td_blockEvents=false; pmc_atlasmg_id=467ca42a-d6ae-4de9-b452-cbed5ed47545; _td_ssc_id=01HZMM6M1FRWQS78NTNXAK9SD8; __browsiSessionID=842abeb3-2e0e-42f2-a856-0981447eda75&false&false&SEARCH&kz&desktop-4.25.21&false; __browsiUID=7d1b1ac4-ec1f-4f3c-8995-46411da75c48; _lr_retry_request=true; _lr_env_src_ats=false; billboard_fonts_loaded=1; _lr_geo_location=KZ; _cc_id=3f4c227604aa1247f71334bf4e56aba4; panoramaId_expiry=1718210255960; panoramaId=a7387dd6c9529ce2ef43d6ef6edd4945a702a1bdbc93bc698e41d70b92355529; panoramaIdType=panoIndiv; _au_1d=AU1D-0100-001717605457-OENMMAH7-V0JI; TAPAD=%7B%22id%22%3A%22e0e1eb5b-b23b-4ce2-abb4-099e677f6143%22%7D; __qca=P0-599749289-1717605461169; _ga_FVWZ0RM4DH=GS1.1.1717606045.1.0.1717606045.60.0.0; _hjSessionUser_2036991=eyJpZCI6IjMwOWViZGY2LTBjN2ItNTE2OS04NjRiLWEzMmRjYmU1N2MyMSIsImNyZWF0ZWQiOjE3MTc2MDU0NTQxNDcsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.2.558969231.1717605453; __pvi=eyJpZCI6InYtMjAyNC0wNi0wNS0yMy0wMS0wOS00MTItRjZSd3NDc3NWcmpsSlNpVS01MDRiNzNjMGY1YTE4YTBiMTYwMjNmMDRmMzAxNDY4YSIsImRvbWFpbiI6Ii5iaWxsYm9hcmQuY29tIiwidGltZSI6MTcxNzYwNjg2OTQxMn0%3D; xbc=%7Bkpex%7DBnIdpzS3aa8aHAptq9RDSQ; __tbc=%7Bkpex%7DcqJsVdztcocBKNdqfNeC6yG6PpzlRPbtx0t3LEI_szgH9s8RDsZysP2oXvsO1sSr; _gat_UA-76834886-1=1; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jun+05+2024+23%3A01%3A10+GMT%2B0600+(Kyrgyzstan+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=9dbeb4d8-50e8-4ca6-aef6-348aa3946ea8&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.billboard.com%2Fc%2Fmusic%2Fmusic-news%2F&groups=C0002%3A1%2CC0004%3A1%2CC0001%3A1%2CC0003%3A1; _ga_DJBCNPKNBT=GS1.1.1717605453.1.1.1717606870.60.0.0; _gat=1; _ga_FCQQWSJ01C=GS1.2.1717605454.1.1.1717606871.0.0.0; _td=b69e3b58-9339-4c98-a414-43aa9f1a3cd5; _awl=2.1717606870.5-e31273dfb4ff98406af791d3dd0219de-6763652d6575726f70652d7765737431-0; _gat_pianoTracker=1; __eoi=ID=e89dfc0516f5db6d:T=1717605456:RT=1717606873:S=AA-AfjbFZazhkpwWcbkRv-_WX0mf; __gads=ID=4a8d301058768919:T=1717605456:RT=1717606873:S=ALNI_MZ6w5FE-7skRN2eZlOxeA9BM55AMQ; __gpi=UID=00000e4b89246758:T=1717605456:RT=1717606873:S=ALNI_MakrE9RFyi2iYFQE_iKMV6Wav3ZlQ; cto_bundle=VoOdQV9rT2glMkJJbjJ4ZzJPUGlvVHUlMkIxdUZGSGRLQU9Heng0R0diYiUyRlBPZkZ2b0NaRDZ5ZTBQT1FLQzhGaTl5S2NEc0Y0c3l4Nkw1dk0zZWpCNW9kRUpDc2ZCYzQ4V2dTTnElMkJPWGJxNzU1dldyJTJGb0ZXV2ZNc2RxdnB3Umg1dVZJWk9NN1ZvcGE2VnZuaHpCN3l3RHVHaWw5Z1I0aXBmNTVabDB0MkhrU2xvQnliJTJCUmVPdU9jTXdOaFJmM3VuVXZ6UCUyRkhzYkJiSWNrMiUyQjNzbkxZRkJNVkcyZUN5QSUzRCUzRA',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

response = requests.get('https://www.billboard.com/c/music/music-news/', headers=headers, cookies=cookies)

src = response.text
# print(src)
soup = BeautifulSoup(src, 'html.parser')

# b = soup.find('a', class_='c-title__link lrv-a-unstyle-link lrv-u-color-brand-primary:hover')
# print(b.text)
def get_music_news_from_web():
  news = soup.find_all('a', class_='c-title__link lrv-a-unstyle-link lrv-u-color-brand-primary:hover')
  return news

news = get_music_news_from_web()

for n in news:
  # print(n.find('a', class_='c-title__link lrv-a-unstyle-link lrv-u-color-brand-primary:hover').text)
  print(n.text.strip())
