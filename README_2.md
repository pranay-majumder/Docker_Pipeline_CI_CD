(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker build -t pranaymajumder17/emotion_analysis_cicd:v1 . 

1e58012b8891ea3ced93337e721ecb6059c9323e6929a  0.6s
 => => exporting manifest list sha256:07f5c6cee60ab73a1a991815846eec8d78d8a7970b7b1891314103387d  0.2s
 => => naming to docker.io/pranaymajumder17/emotion_analysis_cicd:v1                              0.4s
 => => unpacking to docker.io/pranaymajumder17/emotion_analysis_cicd:v1                           1.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/rdzbaujjcjx2ng6ktptxqaltj
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker run -p 8000:8000 -e DAGSHUB_TOKEN=b4387c058c4a46668d72b41accd6ff43ebb69f06 pranaymajumder17/emotion_analysis_cicd:v1
[2026-09-24 18:54:57 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2026-09-24 18:54:57 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2026-09-24 18:54:57 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2026-09-24 18:54:57 +0000] [7] [INFO] Booting worker with pid: 7
[2026-09-24 18:54:57 +0000] [8] [INFO] Booting worker with pid: 8
Downloading artifacts: 100%|██████████| 5/5 [00:02<00:00,  1.75it/s]
Downloading artifacts: 100%|██████████| 5/5 [00:02<00:00,  1.77it/s]
2026/09/24 18:55:26 WARNING mlflow.utils.requirements_utils: Detected one or more mismatches between the model's dependencies and the current Python environment:
 - mlflow (current: 3.15.1, required: mlflow==3.16.1)
 - numpy (current: 2.5.1, required: numpy==2.5.3)
 - pandas (current: 2.3.3, required: pandas==3.0.6)
 - pytest (current: uninstalled, required: pytest==9.1.1)
 - scikit-learn (current: 1.9.0, required: scikit-learn==1.9.1)
 - scipy (current: 1.18.0, required: scipy==1.18.1)
 - skops (current: 0.14.0, required: skops==0.15.0)
To fix the mismatches, call `mlflow.pyfunc.get_model_dependencies(model_uri)` to fetch the model's environment and install dependencies using the resulting environment file.
2026/09/24 18:55:26 WARNING mlflow.utils.requirements_utils: Detected one or more mismatches between the model's dependencies and the current Python environment:
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
[2026-09-24 18:55:47 +0000] [7] [INFO] Started server process [7]
[2026-09-24 18:55:47 +0000] [7] [INFO] Waiting for application startup.
[2026-09-24 18:55:47 +0000] [7] [INFO] Application startup complete.
172.17.0.1:44110 - "GET /docs HTTP/1.1" 200
172.17.0.1:41400 - "GET /docs HTTP/1.1" 200
172.17.0.1:41408 - "GET /docs HTTP/1.1" 200
[2026-09-24 18:55:47 +0000] [8] [INFO] Started server process [8]
[2026-09-24 18:55:47 +0000] [8] [INFO] Waiting for application startup.
[2026-09-24 18:55:47 +0000] [8] [INFO] Application startup complete.
172.17.0.1:41408 - "GET /openapi.json HTTP/1.1" 200
172.17.0.1:39952 - "POST /predict HTTP/1.1" 200
172.17.0.1:36110 - "POST /predict HTTP/1.1" 200
172.17.0.1:59930 - "POST /predict HTTP/1.1" 200
[2026-09-24 19:00:00 +0000] [1] [INFO] Handling signal: int
[2026-09-24 19:00:30 +0000] [1] [ERROR] Worker (pid:8) was sent SIGKILL! Perhaps out of memory?
/usr/local/lib/python3.14/multiprocessing/resource_tracker.py:475: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown: {'/loky-8-n1m0rer1'}
  warnings.warn(
[2026-09-24 19:00:30 +0000] [1] [ERROR] Worker (pid:62) exited with code 1
[2026-09-24 19:00:30 +0000] [1] [ERROR] Worker (pid:62) exited with code 1.
[2026-09-24 19:00:30 +0000] [1] [ERROR] Worker (pid:7) was sent SIGKILL! Perhaps out of memory?
[2026-09-24 19:00:30 +0000] [1] [INFO] Shutting down: Master
/usr/local/lib/python3.14/multiprocessing/resource_tracker.py:475: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown: {'/loky-7-may12mr7'}
  warnings.warn(
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker build -t pranaymajumder17/emotion_analysis_cicd:v1 .                                                                
[+] Building 911.7s (13/13) FINISHED                                              docker:desktop-linux
 => [internal] load build definition from Dockerfile                                              0.3s
 => => transferring dockerfile: 1.05kB                                                            0.1s
 => [internal] load metadata for docker.io/library/python:3.14-slim                               2.4s
 => [auth] library/python:pull token for registry-1.docker.io                                     0.0s
 => [internal] load .dockerignore                                                                 0.1s
 => => transferring context: 2B                                                                   0.1s
 => [1/7] FROM docker.io/library/python:3.14-slim@sha256:caaf356f40667c496d405780745b9ac25771c18  0.1s
 => => resolve docker.io/library/python:3.14-slim@sha256:caaf356f40667c496d405780745b9ac25771c18  0.1s
 => [internal] load build context                                                                 0.1s
 => => transferring context: 608B                                                                 0.1s
 => CACHED [2/7] WORKDIR /app                                                                     0.0s
 => [3/7] COPY fastapi_app/requirements.txt /app/requirements.txt                                 0.1s
 => [4/7] RUN pip install --no-cache-dir -r requirements.txt                                    620.6s
 => [5/7] RUN python -m nltk.downloader stopwords wordnet                                        35.0s
 => [6/7] COPY fastapi_app/ /app/                                                                 1.0s
 => [7/7] COPY models/vectorizer.pkl /app/models/vectorizer.pkl                                   1.3s
 => exporting to image                                                                          248.1s
 => => exporting layers                                                                         182.9s
 => => exporting manifest sha256:11e959ed02dfad1093451fbaa85332b21140e9e5792bdd23f3713f63dcf321d  0.2s
 => => exporting config sha256:5ded53da1a73fb3cf66b005f807328413eac08186a84025dcb041565760ee0b4   0.1s
 => => exporting attestation manifest sha256:6431f8049e67e01b168375b1feabaed3239f2cf6616d2696f6d  0.1s
 => => exporting manifest list sha256:5a64baa39e6d67e47e1767c04639ed71c6573eb624db6b3a91702674d6  0.2s
 => => naming to docker.io/pranaymajumder17/emotion_analysis_cicd:v1                              0.0s
 => => unpacking to docker.io/pranaymajumder17/emotion_analysis_cicd:v1                          64.4s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/ombwlkwnjx7xy40teh35i7toi
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker run -p 8000:8000 -e DAGSHUB_TOKEN=b4387c058c4a46668d72b41accd6ff43ebb69f06 pranaymajumder17/emotion_analysis_cicd:v1
[2026-09-24 19:18:48 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2026-09-24 19:18:48 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2026-09-24 19:18:48 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2026-09-24 19:18:48 +0000] [7] [INFO] Booting worker with pid: 7
[2026-09-24 19:18:48 +0000] [8] [INFO] Booting worker with pid: 8
/usr/local/lib/python3.14/site-packages/sklearn/base.py:525: InconsistentVersionWarning: Trying to unpickle estimator CountVectorizer from version 1.9.0 when using version 1.9.1. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
/usr/local/lib/python3.14/site-packages/sklearn/base.py:525: InconsistentVersionWarning: Trying to unpickle estimator CountVectorizer from version 1.9.0 when using version 1.9.1. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
Downloading artifacts: 100%|██████████| 5/5 [00:02<00:00,  2.26it/s]
Downloading artifacts: 100%|██████████| 5/5 [00:02<00:00,  1.75it/s]
[2026-09-24 19:19:37 +0000] [8] [INFO] Started server process [8]
[2026-09-24 19:19:37 +0000] [8] [INFO] Waiting for application startup.
[2026-09-24 19:19:37 +0000] [8] [INFO] Application startup complete.
[2026-09-24 19:19:37 +0000] [7] [INFO] Started server process [7]
[2026-09-24 19:19:37 +0000] [7] [INFO] Waiting for application startup.
[2026-09-24 19:19:37 +0000] [7] [INFO] Application startup complete.
[2026-09-24 19:41:11 +0000] [1] [INFO] Handling signal: term
[2026-09-24 19:41:11 +0000] [8] [INFO] Shutting down
[2026-09-24 19:41:11 +0000] [8] [INFO] Waiting for application shutdown.
[2026-09-24 19:41:11 +0000] [8] [INFO] Application shutdown complete.
[2026-09-24 19:41:11 +0000] [8] [INFO] Finished server process [8]
[2026-09-24 19:41:11 +0000] [7] [INFO] Shutting down
[2026-09-24 19:41:11 +0000] [1] [ERROR] Worker (pid:8) was sent SIGTERM!
[2026-09-24 19:41:11 +0000] [7] [INFO] Waiting for application shutdown.
[2026-09-24 19:41:11 +0000] [7] [INFO] Application shutdown complete.
[2026-09-24 19:41:11 +0000] [7] [INFO] Finished server process [7]
/usr/local/lib/python3.14/multiprocessing/resource_tracker.py:475: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown: {'/loky-8-eoxd9etk'}
  warnings.warn(
[2026-09-24 19:41:11 +0000] [1] [ERROR] Worker (pid:69) exited with code 1
[2026-09-24 19:41:11 +0000] [1] [ERROR] Worker (pid:69) exited with code 1.
[2026-09-24 19:41:11 +0000] [1] [ERROR] Worker (pid:7) was sent SIGTERM!
[2026-09-24 19:41:11 +0000] [1] [INFO] Shutting down: Master
/usr/local/lib/python3.14/multiprocessing/resource_tracker.py:475: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown: {'/loky-7-tnmsrdyd'}
  warnings.warn(
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .github/workflows/ci.yaml
        modified:   Dockerfile
        deleted:    README.md
        modified:   fastapi_app/app.py
        modified:   fastapi_app/app_async.py
        modified:   fastapi_app/requirements.txt
        modified:   requirements.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README_1.md

no changes added to commit (use "git add" and/or "git commit -a")
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git add .                      
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git commit -m "Adding Workflow"                            
[main c5a9065] Adding Workflow                                  
 8 files changed, 576 insertions(+), 840 deletions(-)
 delete mode 100644 README.md
 create mode 100644 README_1.md
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git push -u origin main
Enumerating objects: 21, done.
Counting objects: 100% (21/21), done.
Delta compression using up to 12 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (12/12), 9.80 KiB | 501.00 KiB/s, done.
Total 12 (delta 5), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (5/5), completed with 5 local objects.
To https://github.com/pranay-majumder/Docker_Pipeline_CI_CD.git
   658a6ca..c5a9065  main -> main
branch 'main' set up to track 'origin/main'.
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker pull pranaymajumder17/emotion_analysis_cicd:latest
latest: Pulling from pranaymajumder17/emotion_analysis_cicd
4f1615dae01f: Pull complete 
8c8e94677f9d: Pull complete 
b0a55bae681e: Pull complete 
e0c193029bf6: Pull complete 
02cc54e15bf0: Pull complete 
7c5c17b927e1: Pull complete 
Digest: sha256:ee2811a227b4e1e67a581d0b515cac1b743c74bdeb8cd2358cc83ed8adf0ef18
Status: Downloaded newer image for pranaymajumder17/emotion_analysis_cicd:latest
docker.io/pranaymajumder17/emotion_analysis_cicd:latest
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker run -p 8000:8000 -e DAGSHUB_TOKEN=b4387c058c4a46668d72b41accd6ff43ebb69f06 pranaymajumder17/emotion_analysis_cicd:latest
[2026-09-24 20:10:18 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2026-09-24 20:10:18 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2026-09-24 20:10:18 +0000] [1] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2026-09-24 20:10:18 +0000] [7] [INFO] Booting worker with pid: 7
[2026-09-24 20:10:18 +0000] [8] [INFO] Booting worker with pid: 8
Downloading artifacts: 100%|██████████| 5/5 [00:02<00:00,  1.90it/s]
Downloading artifacts: 100%|██████████| 5/5 [00:03<00:00,  1.31it/s]
[2026-09-24 20:11:06 +0000] [8] [INFO] Started server process [8]
[2026-09-24 20:11:06 +0000] [8] [INFO] Waiting for application startup.
[2026-09-24 20:11:06 +0000] [8] [INFO] Application startup complete.
[2026-09-24 20:11:07 +0000] [7] [INFO] Started server process [7]
[2026-09-24 20:11:07 +0000] [7] [INFO] Waiting for application startup.
[2026-09-24 20:11:07 +0000] [7] [INFO] Application startup complete.
172.17.0.1:52480 - "GET /docs HTTP/1.1" 200
172.17.0.1:52480 - "GET /openapi.json HTTP/1.1" 200
172.17.0.1:52494 - "POST /predict HTTP/1.1" 200
172.17.0.1:41872 - "POST /predict HTTP/1.1" 200
[2026-09-24 20:12:27 +0000] [1] [INFO] Handling signal: term
[2026-09-24 20:12:27 +0000] [8] [INFO] Shutting down
[2026-09-24 20:12:27 +0000] [7] [INFO] Shutting down
[2026-09-24 20:12:27 +0000] [8] [INFO] Waiting for application shutdown.
[2026-09-24 20:12:27 +0000] [8] [INFO] Application shutdown complete.
[2026-09-24 20:12:27 +0000] [8] [INFO] Finished server process [8]
[2026-09-24 20:12:27 +0000] [7] [INFO] Waiting for application shutdown.
[2026-09-24 20:12:27 +0000] [7] [INFO] Application shutdown complete.
[2026-09-24 20:12:27 +0000] [7] [INFO] Finished server process [7]
[2026-09-24 20:12:27 +0000] [1] [ERROR] Worker (pid:8) was sent SIGTERM!
/usr/local/lib/python3.14/multiprocessing/resource_tracker.py:475: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown: {'/loky-8-ksbb3rgk'}
  warnings.warn(
[2026-09-24 20:12:27 +0000] [1] [ERROR] Worker (pid:7) was sent SIGTERM!
/usr/local/lib/python3.14/multiprocessing/resource_tracker.py:475: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown: {'/loky-7-qnua24f7'}
  warnings.warn(
[2026-09-24 20:12:27 +0000] [1] [ERROR] Worker (pid:62) exited with code 1
[2026-09-24 20:12:27 +0000] [1] [ERROR] Worker (pid:62) exited with code 1.
[2026-09-24 20:12:27 +0000] [1] [ERROR] Worker (pid:69) exited with code 1
[2026-09-24 20:12:27 +0000] [1] [ERROR] Worker (pid:69) exited with code 1.                                                                                                                                                         
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> 


















