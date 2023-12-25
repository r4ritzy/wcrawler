import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError: #this is added if no URL is found with the subdomain
        pass

def mainMethod(url):
    with open("Path/To/wordlist.txt", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            target_url = url
            test_url = target_url + "/" + word
            test_url2 = word + "." + target_url
            response = request(test_url)
            response2 = request(test_url2)
            if response and numeral == 1:
                print("[+] URL Discovered -->> " + test_url)
            
            if response2 and numeral == 2:
                print("[+] URL Discovered -->> " + test_url)                
                

#program starting
print("-- Enter Numeral for the following options : --\n"
        "1 : find paths\n"
        "2: find subdomains")
        
numeral = input("Your Input : ")

if int(numeral) == 1:
    print("You Entered 1; Please Enter URL to find paths")
    url = input("URL : ")
    print("URL =", url)
    mainMethod(url)

if int(numeral) == 2:
    print("You Entered 2; Please Enter URL to find subdomains")
    url = input("URL : ")
    print("URL =", url)
    mainMethod(url)
else :
    print("You Entered Invalid Input")
