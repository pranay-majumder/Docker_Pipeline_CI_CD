
### Create New Github Repo, Make some Initial Commit and Push, after that connect it with Dagshub 
### Dagshub ----> Experiments ----> Mlflow Tracking Server (Experiment Tracking and Model Registry)

### Local Testing ---> Build Docker Image, Run Docker Image, Docker Push (Docker Hub)
### Local Testing ---> FastAPI App Testing

### Pipeline ---> Install Dependency ----> dvc repro (Track Experiment and Regsiter ML Model to Model Registry) ---> Running Test ---> Docker Hub Login ---> Build Docker Image (Image Build on Github VM) ---> Push Image to Docker Hub

### After Successfull Execution of Pipeline your Final image will be Push to Docker Hub so later we can pull this image in our Machine (own Laptop for Local use, EC2 for deployment, ECS) and Run it.

1. (mlops_venv) PS D:\MLOPS> cd Lecture_21_Docker
2. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git init
Initialized empty Git repository in D:/MLOPS/Lecture_21_Docker/.git/
3. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git remote add origin https://github.com/pranay-majumder/Docker_Pipeline_CI_CD.git
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> dvc init
Initialized DVC repository.

You can now commit the changes to git.

+---------------------------------------------------------------------+
|                                                                     |
|        DVC has enabled anonymous aggregate usage analytics.         |
|     Read the analytics documentation (and how to opt-out) here:     |
|             <https://dvc.org/doc/user-guide/analytics>              |
|                                                                     |
+---------------------------------------------------------------------+

What's next?
------------
- Check out the documentation: <https://dvc.org/doc>
- Get help and share ideas: <https://dvc.org/chat>
- Star us on GitHub: <https://github.com/treeverse/dvc>
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .dvc/.gitignore
        new file:   .dvc/config
        new file:   .dvcignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Notes/
        dvc.yaml
        fastapi_app/
        params.yaml
        src/
        test/

4. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git add .

5. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git commit -m "Initial Commit"
[main (root-commit) ca86b22] Initial Commit
 25 files changed, 1227 insertions(+)
 create mode 100644 .dvc/.gitignore
 create mode 100644 .dvc/config
 create mode 100644 .dvcignore
 create mode 100644 Notes/Introduction to Docker.pdf
 create mode 100644 Notes/Pull Docker Image from Docker Hub and Run it using Docker.docx
 create mode 100644 dvc.yaml
 create mode 100644 fastapi_app/__init__.py
 create mode 100644 fastapi_app/__pycache__/__init__.cpython-314.pyc
 create mode 100644 fastapi_app/__pycache__/app.cpython-314.pyc
 create mode 100644 fastapi_app/__pycache__/text_processing.cpython-314.pyc
 create mode 100644 fastapi_app/app.py
 create mode 100644 fastapi_app/text_processing.py
 create mode 100644 params.yaml
 create mode 100644 src/data/data_ingestion.py
 create mode 100644 src/data/data_preprocessing.py
 create mode 100644 src/feature/feature_engineering.py
 create mode 100644 src/model/model_building.py
 create mode 100644 src/model/model_evaluation.py
 create mode 100644 src/model/register_model.py
 create mode 100644 test/__init__.py
 create mode 100644 test/__pycache__/__init__.cpython-314.pyc
 create mode 100644 test/__pycache__/test_fastapi_app.cpython-314.pyc
 create mode 100644 test/__pycache__/test_model.cpython-314.pyc
 create mode 100644 test/test_fastapi_app.py
 create mode 100644 test/test_model.py

6. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git push -u origin main
Enumerating objects: 35, done.
Counting objects: 100% (35/35), done.
Delta compression using up to 12 threads
Compressing objects: 100% (33/33), done.
Writing objects: 100% (35/35), 1.02 MiB | 758.00 KiB/s, done.
Total 35 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/pranay-majumder/Docker_Pipeline_CI_CD.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.


### Running Pipeline (Tracking Experiment and Save ML Model to Model Registry)

7. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> dvc repro
Running stage 'data_ingestion':                                                                                         
> python src/data/data_ingestion.py
2026-09-19 01:55:02,939 - data_ingestion - DEBUG - Parameters loaded from params.yaml
2026-09-19 01:55:11,552 - data_ingestion - DEBUG - Data loaded from https://raw.githubusercontent.com/campusx-official/jupyter-masterclass/main/tweet_emotions.csv
D:\MLOPS\Lecture_21_Docker\src\data\data_ingestion.py:48: FutureWarning: Downcasting behavior in `replace` is deprecatedand will be removed in a future version. To retain the old behavior, explicitly call `result.infer_objects(copy=False)`.To opt-in to the future behavior, set `pd.set_option('future.no_silent_downcasting', True)`
  df["sentiment"] = df["sentiment"].replace({"happiness": 1, "sadness": 0})
2026-09-19 01:55:11,582 - data_ingestion - DEBUG - Data preprocessing completed
2026-09-19 01:55:11,650 - data_ingestion - DEBUG - Train and test data saved to ./data\raw_data
Generating lock file 'dvc.lock'                                                                                         
Updating lock file 'dvc.lock'                                                                                           

Running stage 'data_preprocessing':                                                                                     
> python src/data/data_preprocessing.py
D:\MLOPS\Lecture_21_Docker\src\data\data_preprocessing.py:61: SyntaxWarning: "\s" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\s"? A raw string is also an option.
  text = re.sub('\s+', ' ', text).strip()
[nltk_data] Downloading package wordnet to C:\Users\Pranay
[nltk_data]     Majumder\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
[nltk_data] Downloading package stopwords to C:\Users\Pranay
[nltk_data]     Majumder\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
2026-09-19 01:55:24,308 - data_transformation - DEBUG - data loaded properly
2026-09-19 01:55:24,413 - data_transformation - DEBUG - converted to lower case
2026-09-19 01:56:00,967 - data_transformation - DEBUG - stop words removed
2026-09-19 01:56:01,030 - data_transformation - DEBUG - numbers removed
2026-09-19 01:56:01,162 - data_transformation - DEBUG - punctuations removed
2026-09-19 01:56:01,183 - data_transformation - DEBUG - urls
2026-09-19 01:56:09,597 - data_transformation - DEBUG - lemmatization performed
2026-09-19 01:56:09,598 - data_transformation - DEBUG - Text normalization completed
2026-09-19 01:56:09,609 - data_transformation - DEBUG - converted to lower case
2026-09-19 01:56:16,124 - data_transformation - DEBUG - stop words removed
2026-09-19 01:56:16,134 - data_transformation - DEBUG - numbers removed
2026-09-19 01:56:16,160 - data_transformation - DEBUG - punctuations removed
2026-09-19 01:56:16,198 - data_transformation - DEBUG - urls
2026-09-19 01:56:16,393 - data_transformation - DEBUG - lemmatization performed
2026-09-19 01:56:16,454 - data_transformation - DEBUG - Text normalization completed
2026-09-19 01:56:16,557 - data_transformation - DEBUG - Processed data saved to ./data\processed_data
Updating lock file 'dvc.lock'                                                                                           
                                                                                                                        
Running stage 'feature_engineering':                                                                                    
> python src/feature/feature_engineering.py
2026-09-19 01:56:21,715 - feature_engineering - DEBUG - Parameters loaded from params.yaml
2026-09-19 01:56:21,790 - feature_engineering - DEBUG - Data loaded from ./data/processed_data/train_processed.csv
2026-09-19 01:56:21,834 - feature_engineering - DEBUG - Data loaded from ./data/processed_data/test_processed.csv
2026-09-19 01:56:22,169 - feature_engineering - DEBUG - Bag of Words transformation completed
2026-09-19 01:56:31,209 - feature_engineering - DEBUG - Data saved to ./data/feature_data/train_bow.csv
2026-09-19 01:56:33,308 - feature_engineering - DEBUG - Data saved to ./data/feature_data/test_bow.csv
Updating lock file 'dvc.lock'                                                                                           
                                                                                                                        
Running stage 'model_building':                                                                                         
> python src/model/model_building.py
2026-09-19 01:56:42,841 - model_building - DEBUG - Data loaded from ./data/feature_data/train_bow.csv
D:\MLOPS\mlops_venv\Lib\site-packages\sklearn\linear_model\_logistic.py:1403: FutureWarning: 'penalty' was deprecated inversion 1.8 and will be removed in 1.10. To avoid this warning, leave 'penalty' set to its default value and use 'l1_ratio' or 'C' instead. Use l1_ratio=0 instead of penalty='l2', l1_ratio=1 instead of penalty='l1', l1_ratio set to a float between 0 and 1 instead of penalty='elasticnet', and C=np.inf instead of penalty=None.
  warnings.warn(
2026-09-19 01:56:43,651 - model_building - DEBUG - Model training completed
2026-09-19 01:56:43,661 - model_building - DEBUG - Model saved to models/model.pkl
Updating lock file 'dvc.lock'                                                                                           

Running stage 'model_evaluation':                                                                                       
> python src/model/model_evaluation.py
Traceback (most recent call last):
  File "D:\MLOPS\Lecture_21_Docker\src\model\model_evaluation.py", line 20, in <module>
    raise EnvironmentError("DAGSHUB_TOKEN environment variable is not set")
OSError: DAGSHUB_TOKEN environment variable is not set
ERROR: failed to reproduce 'model_evaluation': failed to run: python src/model/model_evaluation.py, exited with 1
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> dvc repro
Stage 'data_ingestion' didn't change, skipping                                                                          
Stage 'data_preprocessing' didn't change, skipping                                                                      
Stage 'feature_engineering' didn't change, skipping                                                                     
Stage 'model_building' didn't change, skipping                                                                          
Running stage 'model_evaluation':                                                                                       
> python src/model/model_evaluation.py
Accessing as pranay-majumder
Initialized MLflow to track repo "pranay-majumder/Docker_Pipeline_CI_CD"
Repository pranay-majumder/Docker_Pipeline_CI_CD initialized!
2026/09/19 02:04:56 INFO mlflow.tracking.fluent: Experiment with name 'CI_Pipeline' does not exist. Creating a new experiment.
Run name: Bow_LOR_1
2026-09-19 02:05:00,366 - model_evaluation - DEBUG - Model loaded from ./models/model.pkl
2026-09-19 02:05:01,366 - model_evaluation - DEBUG - Data loaded from ./data/feature_data/test_bow.csv
2026-09-19 02:05:01,639 - model_evaluation - DEBUG - Model evaluation completed
2026-09-19 02:05:01,642 - model_evaluation - DEBUG - Metrics saved to reports/metrics.json
2026-09-19 02:05:02,469 - model_evaluation - DEBUG - Parameters loaded from params.yaml
2026/09/19 02:05:02 WARNING mlflow.models.model: `artifact_path` is deprecated. Please use `name` instead.
2026-09-19 02:06:11,667 - model_evaluation - DEBUG - Model info saved to reports/model_info.json
Model evaluation completed: {'accuracy': 0.788433734939759, 'precision': 0.7763915547024952, 'recall': 0.7970443349753694, 'auc': 0.8732781857049913}
🏃 View run Bow_LOR_1 at: https://dagshub.com/pranay-majumder/Docker_Pipeline_CI_CD.mlflow/#/experiments/0/runs/36ed9ff06a4a400e9e3637b0ab8ec555
🧪 View experiment at: https://dagshub.com/pranay-majumder/Docker_Pipeline_CI_CD.mlflow/#/experiments/0
Updating lock file 'dvc.lock'                                                                                           

Running stage 'model_registration':                                                                                     
> python src/model/register_model.py
Accessing as pranay-majumder
Initialized MLflow to track repo "pranay-majumder/Docker_Pipeline_CI_CD"
Repository pranay-majumder/Docker_Pipeline_CI_CD initialized!
2026-09-19 02:06:27,602 - model_registration - DEBUG - Model information loaded from reports/model_info.json

Model Information
-----------------------------
Run ID    : 36ed9ff06a4a400e9e3637b0ab8ec555
Model ID  : m-4a9447a2dbb34d83bb6bd3c2c2352ddf
Model Path: model
Model URI: models:/m-4a9447a2dbb34d83bb6bd3c2c2352ddf
Successfully registered model 'Sentiment_Analysis_BoW_LR'.
2026/09/19 02:06:29 INFO mlflow.store.model_registry.abstract_store: Waiting up to 300 seconds for model version to finish creation. Model name: Sentiment_Analysis_BoW_LR, version 1
Created version '1' of model 'Sentiment_Analysis_BoW_LR'.
2026-09-19 02:06:30,235 - model_registration - DEBUG - Model registered: Sentiment_Analysis_BoW_LR version 1

========================================
Model successfully registered!
========================================
Name       : Sentiment_Analysis_BoW_LR
Version    : 1
Model ID   : m-4a9447a2dbb34d83bb6bd3c2c2352ddf
Version URI: models:/Sentiment_Analysis_BoW_LR/1
Champion   : models:/Sentiment_Analysis_BoW_LR@champion
2026-09-19 02:06:35,631 - model_registration - DEBUG - Model registration completed successfully
Updating lock file 'dvc.lock'                                                                                           

To track the changes with git, run:

        git add dvc.lock 'reports\.gitignore'

To enable auto staging, run:

        dvc config core.autostage true
Use `dvc push` to send your updates to remote storage.

8. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   src/model/model_evaluation.py
        modified:   src/model/register_model.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        data/
        dvc.lock
        errors.log
        feature_engineering_errors.log
        model_building_errors.log
        model_evaluation_errors.log
        model_registration_errors.log
        models/
        reports/
        transformation_errors.log

no changes added to commit (use "git add" and/or "git commit -a")
9. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git add .
10. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git commit -m "First Experiment Done"
[main f3556a7] First Experiment Done
 12 files changed, 148 insertions(+), 23 deletions(-)
 create mode 100644 data/.gitignore
 create mode 100644 dvc.lock
 create mode 100644 errors.log
 create mode 100644 feature_engineering_errors.log
 create mode 100644 model_building_errors.log
 create mode 100644 model_evaluation_errors.log
 create mode 100644 model_registration_errors.log
 create mode 100644 models/.gitignore
 create mode 100644 reports/.gitignore
 create mode 100644 transformation_errors.log

11. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git push -u origin main
Enumerating objects: 19, done.
Counting objects: 100% (19/19), done.
Delta compression using up to 12 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (14/14), 2.59 KiB | 189.00 KiB/s, done.
Total 14 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/pranay-majumder/Docker_Pipeline_CI_CD.git
   ca86b22..f3556a7  main -> main
branch 'main' set up to track 'origin/main'.

### Build Image Localy and Push it to Docker Hub

12. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker --version
Docker version 29.8.0, build 88096ef
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker login
Authenticating with existing credentials... [Username: pranaymajumder17]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'

Login Succeeded

### Build Image Localy, Run The Image Localy and Later Push it to Docker Hub                                                         

13. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker build -t pranaymajumder17/emotion:v1 .                                
[+] Building 45.5s (12/12) FINISHED                                                                 docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                0.4s
 => => transferring dockerfile: 566B                                                                                0.2s
 => [internal] load metadata for docker.io/library/python:3.10-slim                                                 1.7s
 => [internal] load .dockerignore                                                                                   0.0s
 => => transferring context: 2B                                                                                     0.0s
 => [1/7] FROM docker.io/library/python:3.10-slim@sha256:fd76ade0c607f27677bc04be3c60749f400eedc941d9e72967e19a4ce  0.1s
 => => resolve docker.io/library/python:3.10-slim@sha256:fd76ade0c607f27677bc04be3c60749f400eedc941d9e72967e19a4ce  0.1s
 => [internal] load build context                                                                                   0.1s
 => => transferring context: 3.15kB                                                                                 0.0s
 => CACHED [2/7] WORKDIR /app                                                                                       0.0s
 => CACHED [3/7] COPY fastapi_app/requirements.txt /app/requirements.txt                                            0.0s
 => CACHED [4/7] RUN pip install --no-cache-dir -r requirements.txt                                                 0.0s
 => CACHED [5/7] RUN python -m nltk.downloader stopwords wordnet                                                    0.0s
 => [6/7] COPY fastapi_app/ /app/                                                                                   0.1s
 => [7/7] COPY models/vectorizer.pkl /app/models/vectorizer.pkl                                                     0.5s
 => exporting to image                                                                                             41.1s
 => => exporting layers                                                                                             0.5s
 => => exporting manifest sha256:7a02f2bab63dc3313919c1f326aa2300b62d1b573d93e262fc3b3881522076b8                   0.5s
 => => exporting config sha256:b6bd0a88163be7433287ddc63ef914c78b3e2a6867fdba9d9926599a234c6517                     0.2s
 => => exporting attestation manifest sha256:e57c02ca29848b7fce90378afcfcba226c5030f9094bbb101740c04b6b950f88       0.1s
 => => exporting manifest list sha256:33a42f1193fb289199f0859890eca9ed4808462b2198837c771b865eaafc625d              0.1s
 => => naming to docker.io/pranaymajumder17/emotion:v1                                                              0.0s
 => => unpacking to docker.io/pranaymajumder17/emotion:v1                                                          39.4s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/thp567q7m2464uny9cmoysdsa

### Here you need to Provide DAGSHUB_TOKEN (as you use it inside fastapi_app ---> app_async.py)
### Inside "app_async.py" it Load ML model From Model Registry and use it for Prediction

### Run Docker Image Locally

14. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker run -p 8000:8000 -e DAGSHUB_TOKEN=b4387c058c4a46668d72b41accd6ff43ebb69f06 pranaymajumder17/emotion:v1

/usr/local/lib/python3.10/site-packages/sklearn/base.py:442: InconsistentVersionWarning: Trying to unpickle estimator CountVectorizer from version 1.9.0 when using version 1.7.2. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
Downloading artifacts: 100%|██████████| 5/5 [00:02<00:00,  2.05it/s]
2026/09/18 22:19:32 WARNING mlflow.utils.requirements_utils: Detected one or more mismatches between the model's dependencies and the current Python environment:
 - mlflow (current: 3.16.1, required: mlflow==3.16.0)
 - numpy (current: 2.2.6, required: numpy==2.5.3)
 - pandas (current: 2.3.3, required: pandas==3.0.5)
 - psutil (current: uninstalled, required: psutil==7.2.2)
 - pytest (current: uninstalled, required: pytest==9.1.1)
 - scikit-learn (current: 1.7.2, required: scikit-learn==1.9.1)
 - scipy (current: 1.15.3, required: scipy==1.18.1)
 - skops (current: 0.15.0, required: skops==0.14.0)
To fix the mismatches, call `mlflow.pyfunc.get_model_dependencies(model_uri)` to fetch the model's environment and install dependencies using the resulting environment file.
2026/09/18 22:19:32 WARNING mlflow.pyfunc: The version of Python that the model was saved in, `Python 3.14.7`, differs from the version of Python that is currently running, `Python 3.10.21`, and may be incompatible
/usr/local/lib/python3.10/site-packages/sklearn/base.py:442: InconsistentVersionWarning: Trying to unpickle estimator LogisticRegression from version 1.9.1 when using version 1.7.2. This might lead to breaking code or invalid results. Use atyour own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     172.17.0.1:44824 - "GET / HTTP/1.1" 404 Not Found
INFO:     172.17.0.1:44824 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     172.17.0.1:44838 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.17.0.1:44838 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.17.0.1:49888 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.17.0.1:49888 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.17.0.1:49902 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.17.0.1:49902 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.17.0.1:33088 - "POST /predict HTTP/1.1" 500 Internal Server Error
INFO:     172.17.0.1:34128 - "POST /predict HTTP/1.1" 500 Internal Server Error
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [1]


### Run whole Pipeline onetime in oder to test FastApi app Locally

15. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> dvc repro
Stage 'data_ingestion' didn't change, skipping                                                                          
Stage 'data_preprocessing' didn't change, skipping                                                                      
Stage 'feature_engineering' didn't change, skipping                                                                     
Stage 'model_building' didn't change, skipping                                                                          
Running stage 'model_evaluation':                                                                                       
> python src/model/model_evaluation.py
Traceback (most recent call last):
  File "D:\MLOPS\Lecture_21_Docker\src\model\model_evaluation.py", line 25, in <module>
    raise EnvironmentError("DAGSHUB_TOKEN environment variable is not set")
OSError: DAGSHUB_TOKEN environment variable is not set
ERROR: failed to reproduce 'model_evaluation': failed to run: python src/model/model_evaluation.py, exited with 1
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> dvc repro
Stage 'data_ingestion' didn't change, skipping                                                                          
Stage 'data_preprocessing' didn't change, skipping                                                                      
Stage 'feature_engineering' didn't change, skipping                                                                     
Stage 'model_building' didn't change, skipping                                                                          
Stage 'model_evaluation' is cached - skipping run, checking out outputs                                                 
                                                                                                                        
Stage 'model_registration' didn't change, skipping                                                                      
Use `dvc push` to send your updates to remote storage.


### Test fastapi application Localy

17. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> uvicorn fastapi_app.app:app --reload --port 8000                             
INFO:     Will watch for changes in these directories: ['D:\\MLOPS\\Lecture_21_Docker\\fastapi_app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [17776] using StatReload
Accessing as pranay-majumder
Initialized MLflow to track repo "pranay-majumder/Docker_Pipeline_CI_CD"
Repository pranay-majumder/Docker_Pipeline_CI_CD initialized!
Downloading artifacts: 100%|██████████████████████████████████████████████████████████████| 5/5 [00:02<00:00,  2.44it/s]
INFO:     Started server process [15548]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:64381 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:64381 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:56589 - "POST /predict HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [15548]
INFO:     Stopping reloader process [17776]


### Now You have Written Complete Pipeline so Push it to Github
### Github Action will run whole Pipeline (CI Workflow)
 
18. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   dvc.lock
        modified:   fastapi_app/text_processing.py
        modified:   params.yaml
        modified:   src/data/data_preprocessing.py
        modified:   src/model/model_evaluation.py
        modified:   src/model/register_model.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   src/model/model_evaluation.py
        modified:   src/model/register_model.py

no changes added to commit (use "git add" and/or "git commit -a")
19. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git add .
20. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git commit -m "Adding Complete Workflow"
[main a895135] Adding Complete Workflow
 6 files changed, 62 insertions(+), 49 deletions(-)


21. (mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git push -u origin main                 
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 12 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 1.34 KiB | 152.00 KiB/s, done.
Total 9 (delta 7), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (7/7), completed with 7 local objects.
To https://github.com/pranay-majumder/Docker_Pipeline_CI_CD.git
   0640f6a..658a6ca  main -> main
branch 'main' set up to track 'origin/main'.


### In Pipeline We basicaly build Docker Image and Push it to Docker Hub

### So later we basicaly Pull Image from Docker Hub and Run it Localy (Testing Purpose)

22. PS C:\Users\Pranay Majumder> docker pull pranaymajumder17 emotion_analysis_cicd:latest                                                        
latest: Pulling from pranaymajumder17/emotion_analysis_cicd
15a123edf90b: Pull complete
6a1f640c7738: Pull complete 
63bbffdcc418: Pull complete
46f1f1b10021: Pull complete
12f9d99a1aab: Pull complete
7ab94af582c3: Pull complete
Digest: sha256:0726aa115992dfffd85ef0dbbf3bb2944a2f14023755d492518bd8181cf3bd29
Status: Downloaded newer image for pranaymajumder17/emotion_analysis_cicd:latest
docker.io/pranaymajumder17/emotion_analysis_cicd:latest

23. PS C:\Users\Pranay Majumder> docker run -p 8000:8000 -e DAGSHUB_TOKEN=b4387c058c4a46668d72b41accd6ff43ebb69f06 pranaymajumder17/emotion_analysis_cicd:latest
[2026-09-20 20:07:59 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2026-09-20 20:07:59 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2026-09-20 20:07:59 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2026-09-20 20:08:00 +0000] [7] [INFO] Booting worker with pid: 7
[2026-09-20 20:08:00 +0000] [8] [INFO] Booting worker with pid: 8
/usr/local/lib/python3.14/site-packages/sklearn/base.py:525: InconsistentVersionWarning: Trying to unpickle estimator CountVectorizer from version 1.9.1 when using version 1.9.0. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
/usr/local/lib/python3.14/site-packages/sklearn/base.py:525: InconsistentVersionWarning: Trying to unpickle estimator CountVectorizer from version 1.9.1 when using version 1.9.0. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
Downloading artifacts: 100%|██████████| 5/5 [00:03<00:00,  1.66it/s]
Downloading artifacts: 100%|██████████| 5/5 [00:03<00:00,  1.61it/s]
2026/09/20 20:08:23 WARNING mlflow.utils.requirements_utils: Detected one or more mismatches between the model's dependencies and the current Python environment:
 - mlflow (current: 3.15.1, required: mlflow==3.16.1)
 - numpy (current: 2.5.1, required: numpy==2.5.3)
 - pandas (current: 2.3.3, required: pandas==3.0.6)
 - pytest (current: uninstalled, required: pytest==9.1.1)
 - scikit-learn (current: 1.9.0, required: scikit-learn==1.9.1)
 - scipy (current: 1.18.0, required: scipy==1.18.1)
 - skops (current: 0.14.0, required: skops==0.15.0)
To fix the mismatches, call `mlflow.pyfunc.get_model_dependencies(model_uri)` to fetch the model's environment and install dependencies using the resulting environment file.
2026/09/20 20:08:23 WARNING mlflow.utils.requirements_utils: Detected one or more mismatches between the model's dependencies and the current Python environment:
 - mlflow (current: 3.15.1, required: mlflow==3.16.1)
 - numpy (current: 2.5.1, required: numpy==2.5.3)
 - pandas (current: 2.3.3, required: pandas==3.0.6)
 - pytest (current: uninstalled, required: pytest==9.1.1)
 - scikit-learn (current: 1.9.0, required: scikit-learn==1.9.1)
 - scipy (current: 1.18.0, required: scipy==1.18.1)
 - skops (current: 0.14.0, required: skops==0.15.0)
To fix the mismatches, call `mlflow.pyfunc.get_model_dependencies(model_uri)` to fetch the model's environment and install dependencies using the resulting environment file.
/usr/local/lib/python3.14/site-packages/sklearn/base.py:525: InconsistentVersionWarning: Trying to unpickle estimator LogisticRegression from version 1.9.1 when using version 1.9.0. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
/usr/local/lib/python3.14/site-packages/sklearn/base.py:525: InconsistentVersionWarning: Trying to unpickle estimator LogisticRegression from version 1.9.1 when using version 1.9.0. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
[2026-09-20 20:08:46 +0000] [7] [INFO] Started server process [7]
[2026-09-20 20:08:46 +0000] [7] [INFO] Waiting for application startup.
[2026-09-20 20:08:46 +0000] [7] [INFO] Application startup complete.
[2026-09-20 20:08:46 +0000] [8] [INFO] Started server process [8]
[2026-09-20 20:08:46 +0000] [8] [INFO] Waiting for application startup.
[2026-09-20 20:08:46 +0000] [8] [INFO] Application startup complete.
172.17.0.1:37002 - "GET /docs HTTP/1.1" 200
172.17.0.1:37002 - "GET /openapi.json HTTP/1.1" 200
172.17.0.1:37010 - "POST /predict HTTP/1.1" 200
172.17.0.1:48704 - "POST /predict HTTP/1.1" 200
172.17.0.1:57006 - "POST /predict HTTP/1.1" 200
172.17.0.1:35814 - "POST /predict HTTP/1.1" 200
172.17.0.1:47916 - "POST /predict HTTP/1.1" 200
[2026-09-20 20:16:01 +0000] [1] [INFO] Handling signal: int
[2026-09-20 20:16:32 +0000] [1] [ERROR] Worker (pid:7) was sent SIGKILL! Perhaps out of memory?
[2026-09-20 20:16:32 +0000] [1] [ERROR] Worker (pid:8) was sent SIGKILL! Perhaps out of memory?
/usr/local/lib/python3.14/multiprocessing/resource_tracker.py:475: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown: {'/loky-7-1vmlbzd3'}
  warnings.warn(
/usr/local/lib/python3.14/multiprocessing/resource_tracker.py:475: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown: {'/loky-8-gekjf5hc'}
  warnings.warn(
[2026-09-20 20:16:32 +0000] [1] [INFO] Shutting down: Master

PS C:\Users\Pranay Majumder>