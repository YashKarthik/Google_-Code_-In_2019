from shodan import Shodan

api = Shodan('B37FoQIeHcfOarldXp7H7a2vzqZg5BrF')

# Lookup an IP
ipinfo = api.host('8.8.8.8')
print(ipinfo)
