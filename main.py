import os
import sys

from resources.dev import  config
from src.main.download.aws_file_download import S3FileDownloader
from src.main.utility.encrypt_decrypt import decrypt
from src.main.utility.logging_config import logger
from src.main.utility.s3_client_object import S3ClientProvider
from src.main.read.aws_read import *
from src.main.utility.my_sql_session import  *
aws_access_key = config.aws_access_key
aws_secret_key = config.aws_secret_key

s3_client_provider = S3ClientProvider(decrypt(aws_access_key),decrypt(aws_secret_key))
s3_client=s3_client_provider.get_client()

#now u can use s3 client further
response=s3_client.list_buckets()
print(response)
logger.info("list of buckets: %s",response['Buckets'])

# check if local directory has already file present
# If file is present then check the same is available in staging area
# If status as 'A' means active then don't delete the file, try re-run
# Else give an error and don't process the next file

connection = get_mysql_connection()
cursor =connection.cursor()

csv_files=[file for file in os.listdir(config.local_directory) if file.endswith('.csv')]
#formatted=', '.join(f"'{file}'" for file in csv_files)

if csv_files:
    for file in csv_files:
        statement = f"""
        select distinct file_name from {config.properties['database']}.{config.product_staging_table}
        where file_name in ({str(csv_files)[1:-1]}) 
        """

        logger.info(f"dynamically created statement:{statement}")
        cursor.execute(statement)
        data = cursor.fetchall()
        logger.info(f"data is coming:{data}")
        if data:
            logger.info("your last run was fail please check")
        else :
            logger.info("no data found")

else:
    logger.info("your last run was successful")

try:
    s3_reader = S3Reader()
    folder_path=config.s3_source_directory
    s3_absolute_file_path=s3_reader.list_files(s3_client,config.bucket_name,folder_path)
    logger.info("Absolute file path on s3 bucket for csv files %s",s3_absolute_file_path)
    if not s3_absolute_file_path:
        logger.info(f"No files ara available at {folder_path} ")
        raise Exception("No Data available to process")
except Exception as e:
    logger.error("Exited with error:- %s",e)
    raise e

prefix=f"s3://{config.bucket_name}"
file_path= [url[len(prefix):] for url in s3_absolute_file_path]
logging.info("File path is available on s3 under %s bucket and %s folder name",config.bucket_name,folder_path)

try:
    downloader = S3FileDownloader(s3_client,config.bucket_name,config.local_directory)
    downloader.download_files(file_path)
except Exception as e:
    logger.error("File download error: %s",e)
    sys.exit()

#Get a list of all files in loacl diroctry

all_files= os.listdir(config.local_directory)
logger.info(f"List of files present at my local directory after download:{all_files}")

#Filter files with ".csv"  in their names and create absolute path
if all_files:

    error_files=[]
    for files in all_files:
        if files.endswith(".csv"):
            csv_files.append(os.path.abspath(config.local_directory,files))
        else:
            error_files.append(os.path.abspath(config.local_directory,files))


    if not csv_files:
        logger.error("No csv data available to process the request")
        raise Exception("No csv data available to process the request")

else:
    logger.error("There is no data to process")
    raise  Exception("There is no data to process")