from urllib.request import urlopen

url = "http://www.9gag.com"

lien = input("Que recherchez-vous?:")


def get_next_target(content):
	start_index_link = content.find('<a href=')
	if start_index_link == -1:
		return None, 0
	start_index_quote = content.find('"', start_index_link)
	end_ind_quote = content.find('"', start_index_quote + 1)
	url = content[start_index_quote+1:end_ind_quote]
	return url, end_ind_quote

def search_link(list,input):
	s=0
	for el in list:
		if input in el:
			print ("le resulat est:")
			print(el)
			s = s+1
		else:
			pass
	if s==0:
		print ("Désolé, aucun lien retrouvé...")
	
links = []
def print_all_links(page):
	while (True):
		url, end_pos = get_next_target(page)
		if url:
			links.append(url)
			page = page[end_pos:]
		else:
			break
	print ("Please wait while we search...Entering URL now...")
	return links
		
def get_page(page):
	try:
		if page:
			html = urlopen(page).read()
			a = str(html)
			c = print_all_links(a)
			for e in links:
				lol = urlopen(e).read()
				b = str(lol)
				d = print_all_links(b)
	except:
		return ""
	return c, d
		
get_page(url)

print(search_link(links, lien))
