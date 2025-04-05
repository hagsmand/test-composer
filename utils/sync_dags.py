import os
from google.cloud import storage

def sync_dags(composer_bucket):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(composer_bucket)
    dag_folder = "dags/"
    for dag_file in os.listdir(dag_folder):
        if dag_file.endswith(".py"):
            blob = bucket.blob(f"dags/{dag_file}")
            blob.upload_from_filename(os.path.join(dag_folder, dag_file))
            print(f"Uploaded {dag_file} to {composer_bucket}/dags/")

if __name__ == "__main__":
    bucket_name = os.environ.get("COMPOSER_BUCKET")
    sync_dags(bucket_name)
    