from requests import get
from time import time

urls = [
    ("GA-ap-northeast-1", "http://a50c151980ffc4f9b.awsglobalaccelerator.com"),
    ("us-west-2", "http://AGAWo-Appli-F6FYTNC6BC33-2116125174.us-west-2.elb.amazonaws.com"),
    # ("ap-northeast-2", "http://AGAWo-Appli-8DUJWVWZW60T-1230806725.ap-northeast-2.elb.amazonaws.com"),
    # ("ap-northeast-1", "http://AGAWo-Appli-1HHHMI9UBE989-630066877.ap-northeast-1.elb.amazonaws.com"),
]

for url in urls:
    start = time()
    
    for i in range(100):
        result = get(url[1])
    
    print(f"{url[0]}: {(time() - start) / 100}")
