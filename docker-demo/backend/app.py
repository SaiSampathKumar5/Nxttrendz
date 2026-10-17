import os
 
print("nxttrendz backend starting...")
print("Mode:", os.environ.get("APP_ENV"))
 
with open("/app/data/starts.txt", "a") as f:
    f.write("started\n")
 
with open("/app/data/starts.txt") as f:
    print("Times started so far:", len(f.readlines()))