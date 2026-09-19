(mlops_venv) PS D:\MLOPS> cd Lecture_21_Docker
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git init
Initialized empty Git repository in D:/MLOPS/Lecture_21_Docker/.git/
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git remote add origin https://github.com/pranay-majumder/Docker_Pipeline_CI_CD.git
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

(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git add .
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git commit -m "Initial Commit"
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
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git push -u origin main
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
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> dvc repro
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
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git status
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
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git add .
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git commit -m "First Experiment Done"
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
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> git push -u origin main
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
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker --version
Docker version 29.8.0, build 88096ef
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker login
Authenticating with existing credentials... [Username: pranaymajumder17]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker build -t pranaymajumder17/emotion:v1 .
[+] Building 643.3s (12/12) FINISHED                                                                docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                0.8s
 => => transferring dockerfile: 479B                                                                                0.1s
 => [internal] load metadata for docker.io/library/python:3.10-slim                                                 5.6s
 => [auth] library/python:pull token for registry-1.docker.io                                                       0.0s
 => [internal] load .dockerignore                                                                                   0.2s
 => => transferring context: 2B                                                                                     0.0s
 => [internal] load build context                                                                                   0.7s
 => => transferring context: 94.45kB                                                                                0.2s
 => [1/6] FROM docker.io/library/python:3.10-slim@sha256:fd76ade0c607f27677bc04be3c60749f400eedc941d9e72967e19a4c  36.8s
 => => resolve docker.io/library/python:3.10-slim@sha256:fd76ade0c607f27677bc04be3c60749f400eedc941d9e72967e19a4ce  0.5s
 => => sha256:9feb9947eea2d4a7b84504a6ef5ba25f1f86ec5626260c269297140f777beaa0 250B / 250B                          0.7s
 => => sha256:33fd700e5760ffc8c4f8306b7e77aeb159d838d54c855d673df9e81a8ac3f620 13.91MB / 13.91MB                   14.7s
 => => sha256:4bfad29f0e4c54033a1172e7cd01a051cef0fd435105fde568297cccc948e3cc 4.27MB / 4.27MB                      6.9s
 => => sha256:6310eb16bf4251731feab01e8f633bf5e2d75a657ccad97f420b1f83cce457be 29.79MB / 29.79MB                   24.5s
 => => extracting sha256:6310eb16bf4251731feab01e8f633bf5e2d75a657ccad97f420b1f83cce457be                           5.9s
 => => extracting sha256:4bfad29f0e4c54033a1172e7cd01a051cef0fd435105fde568297cccc948e3cc                           1.0s
 => => extracting sha256:33fd700e5760ffc8c4f8306b7e77aeb159d838d54c855d673df9e81a8ac3f620                           3.3s
 => => extracting sha256:9feb9947eea2d4a7b84504a6ef5ba25f1f86ec5626260c269297140f777beaa0                           0.2s
 => [2/6] WORKDIR /app                                                                                              1.0s
 => [3/6] COPY fastapi_app/ /app/                                                                                   0.3s
 => [4/6] COPY models/vectorizer.pkl /app/models/vectorizer.pkl                                                     0.3s
 => [5/6] RUN pip install -r requirements.txt                                                                     384.6s
 => [6/6] RUN python -m nltk.downloader stopwords wordnet                                                          21.0s
 => exporting to image                                                                                            190.5s
 => => exporting layers                                                                                           144.7s
 => => exporting manifest sha256:0a54ea13fca1e6c6534c6f213dfb03873cd1b476cf315b3de7080cffb9be9254                   0.1s
 => => exporting config sha256:e1f8887a13b42df2306062019e2c886f29d65a0d3b417b67f933dfd508942744                     0.1s
 => => exporting attestation manifest sha256:2c710efd18dcd6655cbdb986f82fb1bb8fdf6fbfa98f1f8a96d895213ea3d687       0.1s
 => => exporting manifest list sha256:727a73e3680352da865cc6199c00d376a6bb6eda226248adc33415fe678297b7              0.2s
 => => naming to docker.io/pranaymajumder17/emotion:v1                                                              0.0s
 => => unpacking to docker.io/pranaymajumder17/emotion:v1                                                          45.1s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/yvesgforgr1zat3q7zwdhgv4d
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker run -p 8000:8000 -e DAGSHUB_TOKEN=b4387c058c4a46668d72b41accd6ff43ebb69f06 pranaymajumder17/emotion:v1
Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1631, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1552, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1415, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 910, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/uvicorn/main.py", line 448, in main
    run(
  File "/usr/local/lib/python3.10/site-packages/uvicorn/main.py", line 620, in run
    config.load_app()
  File "/usr/local/lib/python3.10/site-packages/uvicorn/config.py", line 434, in load_app
    return import_from_string(self.app)
  File "/usr/local/lib/python3.10/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.10/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app.py", line 4, in <module>
    import dagshub
ModuleNotFoundError: No module named 'dagshub'

What's next:
    Debug this container error with Gordon → docker ai "help me fix this container error"
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker build -t pranaymajumder17/emotion:v1 .                                
[+] Building 634.2s (13/13) FINISHED                                                                docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                0.1s
 => => transferring dockerfile: 566B                                                                                0.0s
 => [internal] load metadata for docker.io/library/python:3.10-slim                                                 3.7s
 => [auth] library/python:pull token for registry-1.docker.io                                                       0.0s
 => [internal] load .dockerignore                                                                                   0.2s
 => => transferring context: 2B                                                                                     0.1s
 => [1/7] FROM docker.io/library/python:3.10-slim@sha256:fd76ade0c607f27677bc04be3c60749f400eedc941d9e72967e19a4ce  0.1s
 => => resolve docker.io/library/python:3.10-slim@sha256:fd76ade0c607f27677bc04be3c60749f400eedc941d9e72967e19a4ce  0.1s
 => [internal] load build context                                                                                   0.1s
 => => transferring context: 609B                                                                                   0.0s
 => CACHED [2/7] WORKDIR /app                                                                                       0.0s
 => [3/7] COPY fastapi_app/requirements.txt /app/requirements.txt                                                   0.1s
 => [4/7] RUN pip install --no-cache-dir -r requirements.txt                                                      449.9s
 => [5/7] RUN python -m nltk.downloader stopwords wordnet                                                          14.6s
 => [6/7] COPY fastapi_app/ /app/                                                                                   0.3s
 => [7/7] COPY models/vectorizer.pkl /app/models/vectorizer.pkl                                                     0.3s
 => exporting to image                                                                                            163.7s
 => => exporting layers                                                                                           122.9s
 => => exporting manifest sha256:69aad2db868e4a040ed5ecc75463493d040470b409a56a734966b05a05f6b9ae                   0.1s
 => => exporting config sha256:8816c9f48a5213527d6e9eb13db0f80ac7c72e7ad3c9e7356388334d44144a03                     0.1s
 => => exporting attestation manifest sha256:a48f8df716221d269c907b178f0c462d3c11b774119b4e1824d6583b97f632af       0.1s
 => => exporting manifest list sha256:0b2906c423b9426f9ae01708c6e5af302d11416186dd9e7bc2adc23bc414e481              0.1s
 => => naming to docker.io/pranaymajumder17/emotion:v1                                                              0.0s
 => => unpacking to docker.io/pranaymajumder17/emotion:v1                                                          40.3s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/3w4p4b9bsw3z2euqcv57alehe
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker run -p 8000:8000 -e DAGSHUB_TOKEN=b4387c058c4a46668d72b41accd6ff43ebb69f06 pranaymajumder17/emotion:v1
Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1631, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1552, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1415, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 910, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/uvicorn/main.py", line 448, in main
    run(
  File "/usr/local/lib/python3.10/site-packages/uvicorn/main.py", line 620, in run
    config.load_app()
  File "/usr/local/lib/python3.10/site-packages/uvicorn/config.py", line 434, in load_app
    return import_from_string(self.app)
  File "/usr/local/lib/python3.10/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.10/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app.py", line 10, in <module>
    from fastapi_app.text_processing import normalize_text
ModuleNotFoundError: No module named 'fastapi_app'

What's next:
    Debug this container error with Gordon → docker ai "help me fix this container error"
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> cd fastapi_app                  
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker\fastapi_app> uvicorn app:app --reload --port 8000
INFO:     Will watch for changes in these directories: ['D:\\MLOPS\\Lecture_21_Docker\\fastapi_app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [21288] using StatReload
Process SpawnProcess-1:
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\multiprocessing\process.py", line 320, in _bootstrap
    self.run()
    ~~~~~~~~^^
  File "C:\Program Files\Python314\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
    ~~~~~~^^^^^^^^^^^^^^^^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\server.py", line 77, in run
    return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
  File "C:\Program Files\Python314\Lib\asyncio\runners.py", line 205, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "C:\Program Files\Python314\Lib\asyncio\runners.py", line 128, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Program Files\Python314\Lib\asyncio\base_events.py", line 719, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\server.py", line 81, in serve
    await self._serve(sockets)
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\server.py", line 88, in _serve
    config.load()
    ~~~~~~~~~~~^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\config.py", line 494, in load
    self.loaded_app = self.load_app()
                      ~~~~~~~~~~~~~^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\config.py", line 428, in load_app
    return import_from_string(self.app)
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "C:\Program Files\Python314\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1406, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1371, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1342, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 938, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 759, in exec_module
  File "<frozen importlib._bootstrap>", line 491, in _call_with_frames_removed
  File "D:\MLOPS\Lecture_21_Docker\fastapi_app\app.py", line 21, in <module>
    raise EnvironmentError("DAGSHUB_TOKEN environment variable is not set")
OSError: DAGSHUB_TOKEN environment variable is not set
INFO:     Stopping reloader process [21288]
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker\fastapi_app> uvicorn app:app --reload --port 8000
INFO:     Will watch for changes in these directories: ['D:\\MLOPS\\Lecture_21_Docker\\fastapi_app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [7056] using StatReload
Accessing as pranay-majumder
Initialized MLflow to track repo "pranay-majumder/ml-project-using-mlops4"
Repository pranay-majumder/ml-project-using-mlops4 initialized!
Process SpawnProcess-1:
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\multiprocessing\process.py", line 320, in _bootstrap
    self.run()
    ~~~~~~~~^^
  File "C:\Program Files\Python314\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
    ~~~~~~^^^^^^^^^^^^^^^^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\server.py", line 77, in run
    return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
  File "C:\Program Files\Python314\Lib\asyncio\runners.py", line 205, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "C:\Program Files\Python314\Lib\asyncio\runners.py", line 128, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Program Files\Python314\Lib\asyncio\base_events.py", line 719, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\server.py", line 81, in serve
    await self._serve(sockets)
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\server.py", line 88, in _serve
    config.load()
    ~~~~~~~~~~~^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\config.py", line 494, in load
    self.loaded_app = self.load_app()
                      ~~~~~~~~~~~~~^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\config.py", line 428, in load_app
    return import_from_string(self.app)
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "C:\Program Files\Python314\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1406, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1371, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1342, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 938, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 759, in exec_module
  File "<frozen importlib._bootstrap>", line 491, in _call_with_frames_removed
  File "D:\MLOPS\Lecture_21_Docker\fastapi_app\app.py", line 47, in <module>
    with open("./models/vectorizer.pkl", "rb") as file:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: './models/vectorizer.pkl'
INFO:     Stopping reloader process [7056]
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker\fastapi_app> uvicorn app:app --reload --port 8000
INFO:     Will watch for changes in these directories: ['D:\\MLOPS\\Lecture_21_Docker\\fastapi_app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [9440] using StatReload
Accessing as pranay-majumder
Initialized MLflow to track repo "pranay-majumder/ml-project-using-mlops4"
Repository pranay-majumder/ml-project-using-mlops4 initialized!
Process SpawnProcess-1:
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\multiprocessing\process.py", line 320, in _bootstrap
    self.run()
    ~~~~~~~~^^
  File "C:\Program Files\Python314\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
    ~~~~~~^^^^^^^^^^^^^^^^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\server.py", line 77, in run
    return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
  File "C:\Program Files\Python314\Lib\asyncio\runners.py", line 205, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "C:\Program Files\Python314\Lib\asyncio\runners.py", line 128, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Program Files\Python314\Lib\asyncio\base_events.py", line 719, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\server.py", line 81, in serve
    await self._serve(sockets)
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\server.py", line 88, in _serve
    config.load()
    ~~~~~~~~~~~^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\config.py", line 494, in load
    self.loaded_app = self.load_app()
                      ~~~~~~~~~~~~~^^
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\config.py", line 428, in load_app
    return import_from_string(self.app)
  File "D:\MLOPS\mlops_venv\Lib\site-packages\uvicorn\importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "C:\Program Files\Python314\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1406, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1371, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1342, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 938, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 759, in exec_module
  File "<frozen importlib._bootstrap>", line 491, in _call_with_frames_removed
  File "D:\MLOPS\Lecture_21_Docker\fastapi_app\app.py", line 47, in <module>
    with open("./models/vectorizer.pkl", "rb") as file:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: './models/vectorizer.pkl'
WARNING:  StatReload detected changes in 'app.py'. Reloading...
 Accessing as pranay-majumder
Initialized MLflow to track repo "pranay-majumder/ml-project-using-mlops4"
Repository pranay-majumder/ml-project-using-mlops4 initialized!
Downloading artifacts: 100%|██████████████████████████████████████████████████████████████| 5/5 [00:02<00:00,  2.26it/s]
INFO:     Started server process [11640]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:50220 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:50220 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:64598 - "POST /predict HTTP/1.1" 200 OK
INFO:     127.0.0.1:56424 - "POST /predict HTTP/1.1" 200 OK
INFO:     127.0.0.1:50131 - "POST /predict HTTP/1.1" 200 OK
INFO:     127.0.0.1:52360 - "POST /predict HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [11640]
INFO:     Stopping reloader process [9440]
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker\fastapi_app> cd ..                                                            
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker build -t pranaymajumder17/emotion:v1 .                                
[+] Building 58.5s (13/13) FINISHED                                                                 docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                0.1s
 => => transferring dockerfile: 566B                                                                                0.1s
 => [internal] load metadata for docker.io/library/python:3.10-slim                                                 6.0s
 => [auth] library/python:pull token for registry-1.docker.io                                                       0.0s
 => [internal] load .dockerignore                                                                                   0.1s
 => => transferring context: 2B                                                                                     0.0s
 => [1/7] FROM docker.io/library/python:3.10-slim@sha256:fd76ade0c607f27677bc04be3c60749f400eedc941d9e72967e19a4ce  0.2s
 => => resolve docker.io/library/python:3.10-slim@sha256:fd76ade0c607f27677bc04be3c60749f400eedc941d9e72967e19a4ce  0.2s
 => [internal] load build context                                                                                   0.2s
 => => transferring context: 5.93kB                                                                                 0.1s
 => CACHED [2/7] WORKDIR /app                                                                                       0.0s
 => CACHED [3/7] COPY fastapi_app/requirements.txt /app/requirements.txt                                            0.0s
 => CACHED [4/7] RUN pip install --no-cache-dir -r requirements.txt                                                 0.0s
 => CACHED [5/7] RUN python -m nltk.downloader stopwords wordnet                                                    0.0s
 => [6/7] COPY fastapi_app/ /app/                                                                                   0.2s
 => [7/7] COPY models/vectorizer.pkl /app/models/vectorizer.pkl                                                     0.2s
 => exporting to image                                                                                             50.2s
 => => exporting layers                                                                                             1.3s
 => => exporting manifest sha256:1f790a96228e11031e0f82581b33c078a65a7fad34c542dc5963fb4fe12a8ca2                   0.6s
 => => exporting config sha256:70c816a43e42802a9fed40c1de37270a7e9374c91feeb5b936e7c567f6bc5f16                     0.4s
 => => exporting attestation manifest sha256:59f27b1bc8c793f1d00f36065836e752c757c42b5421e10146fcb1e98ed935cc       0.2s
 => => exporting manifest list sha256:b975977954634fd1c6c472c7293c403e0fbf217e5811eac987d697c86741eb4e              0.1s
 => => naming to docker.io/pranaymajumder17/emotion:v1                                                              0.0s
 => => unpacking to docker.io/pranaymajumder17/emotion:v1                                                          47.1s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/wyg7gzck6ichmxasppm3w4oaf
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker run -p 8000:8000 -e DAGSHUB_TOKEN=b4387c058c4a46668d72b41accd6ff43ebb69f06 pranaymajumder17/emotion:v1
Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1631, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1552, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1415, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.10/site-packages/click/core.py", line 910, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/uvicorn/main.py", line 448, in main
    run(
  File "/usr/local/lib/python3.10/site-packages/uvicorn/main.py", line 620, in run
    config.load_app()
  File "/usr/local/lib/python3.10/site-packages/uvicorn/config.py", line 434, in load_app
    return import_from_string(self.app)
  File "/usr/local/lib/python3.10/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app.py", line 48, in <module>
    with open("vectorizer.pkl", "rb") as file:
FileNotFoundError: [Errno 2] No such file or directory: 'vectorizer.pkl'

What's next:
    Debug this container error with Gordon → docker ai "help me fix this container error"
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker build -t pranaymajumder17/emotion:v1 .                                
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
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker run -p 8000:8000 -e DAGSHUB_TOKEN=b4387c058c4a46668d72b41accd6ff43ebb69f06 pranaymajumder17/emotion:v1
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
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> dvc repro
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
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> cd fastapi_app
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker\fastapi_app> uvicorn app:app --reload --port 8000                             
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
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker\fastapi_app> docker build -t pranaymajumder17/emotion:v1 .                    
[+] Building 0.4s (1/1) FINISHED                                                                    docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                0.3s
 => => transferring dockerfile: 2B                                                                                  0.0s
ERROR: failed to build: failed to solve: failed to read dockerfile: open Dockerfile: no such file or directory

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/ts331ns442kxke5ji8nvx2k13

What's next:
    Debug this build failure with Gordon → docker ai "help me fix this build failure"
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker\fastapi_app> cd..
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker build -t pranaymajumder17/emotion:v1 .
[+] Building 606.4s (13/13) FINISHED                                                                docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                0.1s
 => => transferring dockerfile: 566B                                                                                0.0s
 => [internal] load metadata for docker.io/library/python:3.14-slim                                                 4.1s
 => [auth] library/python:pull token for registry-1.docker.io                                                       0.0s
 => [internal] load .dockerignore                                                                                   0.0s
 => => transferring context: 2B                                                                                     0.0s
 => [1/7] FROM docker.io/library/python:3.14-slim@sha256:cad9a2c871761c413caa6fdd6441c783451e740a48aaeba60ae62a8b  10.5s
 => => resolve docker.io/library/python:3.14-slim@sha256:cad9a2c871761c413caa6fdd6441c783451e740a48aaeba60ae62a8b5  0.1s
 => => sha256:3d2c3ff37d4c435d5db82ae37f1d8be56f8feb24320349f5c8c62df7624a5ee2 249B / 249B                          0.5s
 => => sha256:6bd54ebeb5af95e8f880bffc616ee55c0f3eb181b194388a2c9fd92be54a5048 12.36MB / 12.36MB                    7.5s
 => => sha256:d4a378e57055fa2c97715602c4073a0d034e89b0dc29ef17bcc30f9692233049 4.27MB / 4.27MB                      5.4s
 => => extracting sha256:d4a378e57055fa2c97715602c4073a0d034e89b0dc29ef17bcc30f9692233049                           0.8s
 => => extracting sha256:6bd54ebeb5af95e8f880bffc616ee55c0f3eb181b194388a2c9fd92be54a5048                           2.0s
 => => extracting sha256:3d2c3ff37d4c435d5db82ae37f1d8be56f8feb24320349f5c8c62df7624a5ee2                           0.2s
 => [internal] load build context                                                                                   0.1s
 => => transferring context: 6.09kB                                                                                 0.0s
 => [2/7] WORKDIR /app                                                                                              0.4s
 => [3/7] COPY fastapi_app/requirements.txt /app/requirements.txt                                                   0.3s
 => [4/7] RUN pip install --no-cache-dir -r requirements.txt                                                      385.8s
 => [5/7] RUN python -m nltk.downloader stopwords wordnet                                                          29.4s
 => [6/7] COPY fastapi_app/ /app/                                                                                   0.2s
 => [7/7] COPY models/vectorizer.pkl /app/models/vectorizer.pkl                                                     0.3s
 => exporting to image                                                                                            173.2s
 => => exporting layers                                                                                           126.1s
 => => exporting manifest sha256:396d63028c9935af34a2125784e34e5431080427a0baf59ca036fbec12ea04c4                   0.5s
 => => exporting config sha256:949469e4e4dbfe738c53b9c444d21688720013389e4c6a1078c64b9af485b718                     0.1s
 => => exporting attestation manifest sha256:add6f9fa44107adffe0c065ec46c546e270ac65cce090750d3ea7fec8766e225       0.3s
 => => exporting manifest list sha256:ee9854c05e82bbaa882646558ab45288d388d15f4400912e45b3039a5fdd5cbf              0.1s
 => => naming to docker.io/pranaymajumder17/emotion:v1                                                              0.0s
 => => unpacking to docker.io/pranaymajumder17/emotion:v1                                                          46.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/y02g2p30r6jq44tvlog3o1br9
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> docker run -p 8000:8000 -e DAGSHUB_TOKEN=b4387c058c4a46668d72b41accd6ff43ebb69f06 pranaymajumder17/emotion:v1
/usr/local/lib/python3.14/site-packages/sklearn/base.py:525: InconsistentVersionWarning: Trying to unpickle estimator CountVectorizer from version 1.9.0 when using version 1.9.1. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
Downloading artifacts: 100%|██████████| 5/5 [00:02<00:00,  2.19it/s]
2026/09/18 22:48:15 WARNING mlflow.utils.requirements_utils: Detected one or more mismatches between the model's dependencies and the current Python environment:
 - mlflow (current: 3.16.1, required: mlflow==3.16.0)
 - pandas (current: 3.0.6, required: pandas==3.0.5)
 - psutil (current: uninstalled, required: psutil==7.2.2)
 - pytest (current: uninstalled, required: pytest==9.1.1)
 - skops (current: 0.15.0, required: skops==0.14.0)
To fix the mismatches, call `mlflow.pyfunc.get_model_dependencies(model_uri)` to fetch the model's environment and install dependencies using the resulting environment file.
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     172.17.0.1:38818 - "GET / HTTP/1.1" 404 Not Found
INFO:     172.17.0.1:38824 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.17.0.1:38824 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.17.0.1:50364 - "POST /predict HTTP/1.1" 500 Internal Server Error
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [1]
(mlops_venv) PS D:\MLOPS\Lecture_21_Docker> New Change