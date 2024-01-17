import os 
from clarifai.client.dataset import Dataset

#read in the token 
os.environ['CLARIFAI_PAT'] = "db67a1ed7426480c92b2c255664f79d1"


#replace your "user_id", "app_id", "dataset_id".
dataset = Dataset(user_id="shariqmalik10", app_id="test-app", dataset_id="test-app-dataset-1")

#enter the folder path. Try to enter a relative path if possible 
dataset.upload_from_folder(folder_path='folder_path', input_type='text', labels=True)

