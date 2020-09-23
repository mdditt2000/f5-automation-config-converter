# Project Charon - Building out Light / MVP

docker load -i f5-appsvcs-charon-1.6.0.tar.gz
docker run --rm -v "$PWD":/app/data f5-appsvcs-charon:1.5.0 -o data/TLS_Encryptionv2.json -u data/TLS_Encryptionv2.ucs