import requests

#r = requests.get("https://api.ipify.org") #what your external IP address is
r = requests.get("https://byu-cpe.github.io/ComputingBootCamp/media/example_data_big.csv") 

print(r.text) 
