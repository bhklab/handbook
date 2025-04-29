# **Google Cloud Vertex AI**

Vertex AI is Google Cloud’s end-to-end platform for building, training, deploying, and managing machine learning models.

## **Why Use Vertex AI?**

- Unified platform for ML workflows: training, tuning, deploying, and monitoring models.
- Integrated with other GCP services like GCS and BigQuery.
- Supports custom models, AutoML, and pre-trained models.
- Built-in MLOps tools for tracking experiments, model versions, and pipelines.

## **Main Features of Vertex AI**

### **Training**: Train custom models with Vertex AI
Vertex AI enables you to train machine learning models using pre-built containers (for frameworks like TensorFlow, PyTorch, XGBoost) or your custom containers. You can configure distributed training, use accelerators (GPUs/TPUs), and tune hyperparameters automatically.  
To start training:
- Go to **Vertex AI > Training** in the GCP console.
- Choose between **Custom Training**, **AutoML**, or **Pre-trained models**.
- Specify your dataset, training script (if custom), and machine type.

### **Workbench**: Managed Jupyter notebooks integrated with GCP resources.
Setting Up and Using Vertex AI Workbench
- Go to the "Vertex AI Workbench" in the GCP console.
- Click **New Notebook**.
- Select:
  - **Environment** (e.g., TensorFlow Enterprise, PyTorch).
  - **Machine Type** (CPU or GPU).
- After creation, click **Open JupyterLab** to start working.
You can also start and stop notebooks as needed to control costs.

### **Model Monitoring** : Track model performance.
Vertex AI includes a built-in experiment tracking tool called **Vertex AI Experiments**. It automatically or manually tracks ML training runs and logs:
  - Hyperparameters (e.g., learning rate, batch size)
  - Evaluation metrics (e.g., accuracy, loss)
  - Artifacts (e.g., model files)
  - Environment details (e.g., container, machine type)
To use it you can:
- Automatically tracks runs from **Vertex AI Workbench**.
- You can also log metrics programmatically using the Python SDK.

### **Prediction and Deployment**: Serve models
Vertex AI provides two ways to serve models: **online prediction** (real-time requests) and **batch prediction** (large-scale async jobs). You can deploy trained models to an endpoint with autoscaling and version management.  
To deploy a model:
- Go to **Vertex AI > Models**.
- Upload or select your model and deploy it to an endpoint.
- Set machine type and scaling options.

### **Feature Store**: Manage and serve ML features
Vertex AI Feature Store provides a centralized repository to manage, reuse, and serve ML features for training and online inference. It ensures consistency between training and serving data.  
To use Feature Store:
- Create a Featurestore in **Vertex AI Feature Store**.
- Define entity types and features.
- Ingest data manually or set up ingestion pipelines.

### **Pipelines**: Automate and orchestrate ML workflows
Vertex AI Pipelines allow you to build reproducible, scalable ML workflows by chaining steps like data processing, training, evaluation, and deployment. Based on Kubeflow Pipelines, it helps manage experiment runs and simplifies MLOps.  
To create a pipeline:
- Define your steps using **Vertex Pipelines SDK**.
- Upload and run the pipeline through **Vertex AI Pipelines**.
- Monitor executions directly in the console.

  You can find detailed information and tutorials about Vertex AI in the official: https://cloud.google.com/vertex-ai/docs
  
