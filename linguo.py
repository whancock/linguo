from requests import Request, Session
from lxml import html, etree




s = Session()



# data = {
# 	"corpus": "us",
# 	"z1": "xxx"
# }

# request = Request('POST', 'http://googlebooks.byu.edu/x.asp', params=data)
# prepped = s.prepare_request(request)
# response = s.send(prepped)



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36',
    'Cookie': 'ASPSESSIONIDAABQBCTB=OLKDCFLAMOCHLGNENENHHOBA;'
}


data = {
	"f": "coll", 
	"w1": "wedding", 
	"w2": "[nn*]",
	"wl": "2",
	"wr": "2"
}

url = 'http://googlebooks.byu.edu/x2.asp'




request = Request('GET', url, headers=headers, params=data)
prepped = s.prepare_request(request)
response = s.send(prepped)

print(response.content)


tree = html.fromstring(response.content)
table = tree.xpath('/html/body/table[2]/tr')


for item in table[1:-1]:

	if item is not None :
		
		count = item.xpath('./td[4]//text()')[0]
		word = item.xpath('./td[2]//text()')[2]

		print(count, word)
