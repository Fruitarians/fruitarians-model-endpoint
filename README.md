# Fruitarians - Machine Learning Operations Deployment with CI/CD

_The machine learning technology used in Fruitarians for deployment_

**Powered by:**

<p style="text-align: center; background-color: #eee; display: inline-block; padding: 14px 20px; border-radius: 15px;">
<img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/TensorFlow_logo.svg" width="250"/>
</p>

MLOps (Machine Learning Operations) combines the principles of CI/CD with machine learning workflows to establish a robust and automated pipeline for developing, deploying, and maintaining machine learning models. Here's how MLOps integrates with CI/CD:
- Continuous Integration (CI): Developers collaborate using version control systems like Git, where they commit code changes, model updates, and other related assets. CI systems, such as Google Cloud Build (GCB), monitor the repository for changes and trigger the build process.
- Build Process: The CI system fetches the latest code and data from the repository and initiates the build process. For machine learning models built with TensorFlow, the process may involve preparing the data, training the model, and generating artifacts like saved model files.
- Testing: Automated tests are performed on the built model to validate its functionality and performance. These tests can include unit tests, integration tests, and tests specific to the model's evaluation metrics. The CI system, such as GCB, executes these tests to ensure the model meets the desired quality standards.
- Continuous Deployment (CD): If the tests pass, the CD pipeline takes over. In the context of MLOps, the deployment typically involves packaging the trained model into a container using Docker. The container image is then deployed to an execution environment like Google Cloud Run.
- Cloud Run Deployment: Cloud Run provides a serverless platform for deploying and serving containerized applications, including machine learning models. The deployed model becomes accessible through a REST API endpoint, allowing users to make predictions or perform inferences.
- Monitoring and Logging: MLOps incorporates monitoring and logging mechanisms to track the deployed model's performance, usage, and errors. This data helps in identifying issues, optimizing resource allocation, and ensuring the model operates as expected in the production environment.
- Versioning and Rollbacks: MLOps emphasizes version control for models, ensuring traceability and reproducibility. Different model versions are managed, allowing easy rollbacks if necessary. This enables efficient experimentation, model comparisons, and the ability to revert to a previous version if issues arise.
- Automated Retraining and Updates: MLOps enables automated retraining and updates of machine learning models. Whenever new data becomes available or model performance deteriorates, triggers can be set up to retrain the model and redeploy it seamlessly within the CI/CD pipeline.

By combining CI/CD with MLOps practices, organizations can establish a streamlined and automated pipeline for machine learning development, deployment, and maintenance. This ensures continuous improvement, reproducibility, scalability, and reliable delivery of machine learning solutions.

The machine learning technology that used in CI/CD model:

-   **FastAPI**: A Python framework for building fast and efficient Backend APIs.
-   **Docker**: Used to package the application and its dependencies into isolated containers.
-   **Github**: A popular platform for version control and hosting the application's source code.
-   **Google Cloud Build**: A CI/CD management service provided by Google Cloud Platform.
-   **Google Cloud Run**: A serverless computing service used to deploy and run applications in containers.


## Technology Used

There are five technologies we use in the **Fruitarians** Machine Learning Operations Deployment with CI/CD: FastAPI, Docker, Github, Google Cloud Build, Google Cloud Run.

### FastAPI

<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="100"/>

FastAPI can be used to deploy a machine learning model:
- *Model Training*: Train your machine learning model using libraries like TensorFlow. This involves feeding the model with relevant data and optimizing it to make accurate predictions.
- *FastAPI Integration*: Integrate the trained model into a FastAPI application. Define API endpoints that will receive input data and return model predictions.
- *Request Handling*: Define request handling functions in FastAPI that will receive incoming requests containing input data. These functions will preprocess the input, pass it to the trained model for prediction, and return the model's response.
- *API Documentation*: FastAPI automatically generates documentation for your API based on type annotations and function descriptions. This documentation provides details on the API endpoints, expected input formats, and response structures.
- *Deployment*: Deploy the FastAPI application to a hosting platform or server. Platforms like Google Cloud Run or Heroku make it easy to deploy and manage FastAPI applications.
- *Testing and Monitoring*: Test the deployed API to ensure it's functioning as expected. Monitor the API's performance, track usage metrics, and log any errors or issues for debugging and improvement.

My endpoint:

```YAML
GET /: This is the root endpoint that returns a default response when accessed with a GET request. It can be used for testing or to provide general information about the API. Ex "Welcome to the Fruitarians API for freshness!".

POST /api/prediction/: This endpoint is used for making predictions. It expects a JSON payload containing an image in the request body. The image is preprocessed, passed through the trained image classification model, and the predicted fruit freshness is returned as the API response.
```

Docs: [fastapi-docs](https://fastapi.tiangolo.com/)

### Docker 

<img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" width="100"/>

The provided code is a Dockerfile, which is used to build a Docker image for the deployment of a machine learning model using FastAPI. Here's a brief explanation of the different sections in the Dockerfile:

```YAML
FROM python:3.11.2-slim-buster: Specifies the base image for the Docker image, which is Python 3.11.2 with a slim version of the Debian Buster operating system.
RUN mkdir -p /fruitarians-model and WORKDIR /fruitarians-model: Creates a directory named "fruitarians-model" inside the Docker image and sets it as the working directory.
RUN pip install --no-cache-dir -U pip: Upgrades pip, the package installer for Python, to the latest version.
COPY requirements.txt .: Copies the requirements.txt file from the local directory to the Docker image's working directory.
RUN pip install -r requirements.txt: Installs the Python packages listed in the requirements.txt file using pip.
COPY . .: Copies the entire content of the local directory to the Docker image's working directory.
CMD ["python", "main.py"]: Specifies the command to run when the Docker container is started, which in this case is executing the main.py Python file.
```

The Dockerfile sets up a Python environment, installs the required dependencies specified in the requirements.txt file, and copies the application code into the Docker image. When the Docker container is run, it will execute the main.py file, which is assumed to contain the FastAPI application code for serving the machine learning model.

Docs:
[docker-docs](https://docs.docker.com/)

### Github

<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="100"/>

GitHub is utilized to create triggers in Google Cloud Build for deploying a machine learning model using CI/CD on Cloud Run. The repository at  **`https://github.com/Fruitarians/fruitarians-model-endpoint`** contains the necessary code and configuration files for the deployment process. With the triggers set up, any changes or updates made to the repository will automatically trigger the CI/CD pipeline in Google Cloud Build, which will build and deploy the model to Cloud Run based on the defined configuration. This integration allows for streamlined development, version control, and automated deployment of the machine learning model using the power of GitHub and Google Cloud technologies.

Docs: [github-docs](https://docs.github.com/en)

### Google Cloud Build 

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs3WdMUSzoZGaJjfWjioiK8oQSNFuNUdlty1ocOgsceQ&s" width="100"/>

Google Cloud Build is a CI/CD management service provided by Google Cloud Platform. It is used to automate the process of building, testing, and deploying applications. In the given steps, Cloud Build is utilized to automate the deployment of a machine learning model to Google Cloud Run.

The provided steps outline the CI/CD pipeline for deploying the model:

1. Step 1: Building the container image - The Docker image is built using the specified Dockerfile, and the resulting image is tagged with the project ID and image name.
2. Step 2: Pushing the container image to Container Registry - The built container image is pushed to the Container Registry, making it accessible for deployment.
3. Step 3: Deploying the container to Cloud Run - The container image is deployed to Cloud Run, specifying the image location, region, platform, and authentication settings.
   
To create a trigger for this CI/CD pipeline, the trigger name would be **`fruitarians-model-endpoint`** . This trigger can be set up in Google Cloud Build to monitor changes in the repository or other specified conditions. Once the trigger is activated, it will initiate the defined CI/CD pipeline, automatically building and deploying the model to Cloud Run.

Google Cloud Build is used to automate the deployment process, from building the container image to deploying it to Cloud Run, enabling efficient and streamlined CI/CD for the machine learning model.

Docs: [cloud-build-docs](https://cloud.google.com/build/docs)

### Google Cloud Build 

<img src="https://static-00.iconduck.com/assets.00/google-cloud-run-icon-512x460-knkc4eyx.png" width="100"/>

Google Cloud Run is a serverless compute service used to run containerized applications. In this implementation, Cloud Run is used to run a container that contains a machine learning model and an API endpoint. This allows for easy and scalable exposure of the model through an HTTP API.

The service or endpoint name in this case is "fruitarians-model-endpoint". This is the name given to the deployed service on Cloud Run. It will expose the machine learning model and API through an HTTP endpoint, allowing external clients to make predictions or interact with the model.

Docs: [cloud-run-docs](https://cloud.google.com/run/docs)

# How to use
You can try
```YAML
https://fruitarians-model-endpoint-cwdelhrmna-et.a.run.app/docs/
```

CC23-4S448 ML Teams.
