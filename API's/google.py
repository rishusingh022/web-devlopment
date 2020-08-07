import requests

def main():
	res=requests.get("https://www.google.com/")
	print(res.text)
	# res-response resuest.get is fuction that is goingt 
	#to take url as input

if __name__ == "__main__":
	main()