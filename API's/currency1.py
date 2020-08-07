import requests

def main():
	res = requests.get("http://data.fixer.io/api/latest?access_key=apikey&base=USD&symbols=EUR")
	if res.status_code!=200:
		raise Exception("error:api request unsuccessfull")
	data=res.json()
	rate=data["rates"]["EUR"]
	print(f"1 usd is = {rate} EUR")

if __name__ == "__main__":
	main()