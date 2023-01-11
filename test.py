from eksisozluk.EksiSozluk import EksiApi

# or EksiApi(username, password)
client = EksiApi()

entry = client.get_entry("1")
print(entry)
