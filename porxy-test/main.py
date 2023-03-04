import requests
import concurrent.futures
from colorama import init, Fore

def check_proxy(proxy):
    url = 'https://httpbin.org/ip'
    proxies = {'http': proxy, 'https': proxy}

    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        print(Fore.GREEN + f"sucess     {proxy}")
        with open('live.txt', 'a+') as f:
            f.write(f'{proxy}\n')
    except:
        print(Fore.RED +  f"failed     {proxy}")

def check_proxy_list(file_path):
    with open(file_path) as f:
        proxies = f.read().splitlines()
    return proxies


# Example usage
def thed(proxies):
    working_proxies = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(check_proxy, proxies)

    for proxy, result in zip(proxies, results):
        if result:
            working_proxies.append(proxy)
    return working_proxies


file_path = 'lista.txt'
working_proxies = check_proxy_list(file_path)
thed(working_proxies)
print(Fore.WHITE + f'Foram testado {len(working_proxies)} proxies')