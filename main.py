import json

sites = [ ]

for url in open("urls.txt"):
    url = url.strip()
    if not url: continue
    site = { }
    site['url'] = url
    site['baseDomain'] = url.split("/")[2]
    site['frecency'] = 100
    site['lastVisitDate'] = 1459200130160413
    site['title'] = site['baseDomain'].split(".")[-2]
    if site['title'] in ['co']:
        site['title'] = site['baseDomain'].split(".")[-3]
    site['type'] = 'history'
    sites.append(site)

print(json.dumps(sites))
