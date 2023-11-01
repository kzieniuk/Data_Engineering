import json
import random
from minio import Minio
from minio.error import S3Error

minio_server = "localhost:9000"
minio_access_key = "Y4DI113KQgqz60JScuMd"
minio_secret_key = "CLRH00BBFiYFCqFkP14WqN9EqYel7OX7nIMfOozy"
minio_bucket = "dinos"

client = Minio(minio_server, access_key=minio_access_key, secret_key=minio_secret_key, secure=False)

try:
    client.fput_object(minio_bucket, "dinosaur_data.json", "dinosaur_data.json")
    print("Dinosaur data uploaded to MinIO server.")
except S3Error as e:
    print(f"Error uploading to MinIO: {e}")
