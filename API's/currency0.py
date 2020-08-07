import requests

def main():
	res = requests.get("http://data.fixer.io/api/latest?access_key=apikey&base=USD&symbols=EUR")
	if res.status_code!=200:
		raise Exception("error:api request unsuccessfull")
	data=res.json()
	print(data)	

if __name__ == "__main__":
	main()