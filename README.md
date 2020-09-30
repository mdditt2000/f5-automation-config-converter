# Project Charon - Building out Light / MVP

docker load -i f5-appsvcs-charon-1.6.0.tar.gz
docker run --rm -v "$PWD":/app/data f5-appsvcs-charon:1.6.0 -o data/TLS_Encryptionv2.json -u data/TLS_Encryptionv2.ucs


- Install Python Docker to run python script to make the diff:
```
docker build -t f5-ansible-runner .
docker run -t f5-ansible-runner python3 --version
```

- Json diff between **as3_from_bigip.json** and **as3_from_charon.json**, make sure both files are located in **data/** folder.
```
./helper python3 /ansible/as3_diff.py --version charon1.6.0-v1
```