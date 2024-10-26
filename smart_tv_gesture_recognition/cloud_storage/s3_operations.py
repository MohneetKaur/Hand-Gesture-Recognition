import os
import sys
from exception import HandException

class S3Operation:
    def sync_folder_to_s3(self, folder:str, bucket_name:str, bucket_folder_name:str) -> None:
        try:
            command: str = (
                f"AWS S3 sync {folder} s3://{bucket_name}/{bucket_folder_name}/'"
            )
            os.system(command)
        
        except Exception as e:
            raise HandException(e, sys)
        
    
    def sync_folder_from_s3(self, folder:str, bucket_name:str, bucket_folder_name:str) -> None:
        try:
            command: str = (
                f'AWS S3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder}'
            )
            os.system(command)
        except Exception as e:
            raise HandException(e, sys)