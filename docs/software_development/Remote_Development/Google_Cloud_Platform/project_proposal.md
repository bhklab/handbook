
# **GCP Project Proposal**

----------

## **1. Introduction**

This proposal outlines the process of **creating a new GCP project**, selecting the **required services**, and **estimating costs**. The document will also provide **official GCP links** for each service to help project members explore details and pricing.

----------

## **2. Project Objectives**

-   Set up a **scalable GCP environment** to support data processing, ML training, and web deployment.
    
-   Select **appropriate GCP services** based on project needs.
    
-   Estimate **costs** for each service using **GCP Pricing Calculator**.
    
-   Optimize resource allocation to **stay within budget**.
  

----------

## **3. Getting Started with GCP Project**

To create a new project in GCP:

1.  Go to **GCP Console**
    
2.  Click **“Select a Project”** → **“New Project”**
    
3.  Enter:
    
    -   **Project Name** → e.g., `aircheck`
        
    -   **Organization** → Your organization name (if any)
        
    -   **Billing Account** → Link a billing account
        
4.  Enable required APIs (e.g., GCS bucket, BigQuery, Dataproc, etc.)
    
5.  Set up **IAM roles** for team members.
    

**Please refer this for detail information:** [GCP Create Project Documentation](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

----------


## **4. Estimating GCP Costs**

GCP provides a **Pricing Calculator** to estimate project costs based on resource usage.

### **Steps to Estimate Costs**

1.  Open **[GCP Pricing Calculator](https://cloud.google.com/products/calculator)**
    
2.  Select the required services (e.g., Cloud Storage, Compute Engine, BigQuery, Dataproc)
    
3.  Enter expected usage details:
    
    -   **Region**
    
    -    **Location**
        
    -   **Storage class**
        
    -   **Total amount of storage**
   
     
 5. You can add additional services by clicking **“Add to Estimate”** and selecting   		the required services.    
4.  Download the cost estimate as a **PDF** for reporting.
    

**Example Cost Estimation:**


| Service | Resource Type | Monthly Estimate | Annual Estimate |
|---------|---------------|:----------------:|:---------------:|
| Vertex AI | 4 vCPUs, 16GB RAM, 50 hrs | **$200** | **$2,400** |
| Dataproc | 3 nodes, 4 vCPUs each | **$300** | **$3,600** |
| BigQuery | 1 TB storage, 50GB queries | **$50** | **$600** |
| GCS | 500GB storage | **$20** | **$240** |
| Cloud Run | 1 instance, 10k requests | **$15** | **$180** |
| **Total** | — | **$585** | **$7,020** |
----------

## **5. Service Selection Strategy**

Before selecting GCP services, follow these steps:

1.  **Identify the Use Case** → e.g., data processing, ML model training, hosting dashboards.
    
2.  **Map Required Services** → Choose GCP products based on needs.
    
3.  **Check Pricing** → Use the GCP pricing calculator for initial estimates.
    
4.  **Optimize Costs** → Use autoscaling, serverless options, and resource quotas to avoid overuse.
    
5.  **Monitor Spending** → Set up GCP Budgets & Alerts to track costs.
    

----------

## **6. Useful References**

-   [GCP Free Tier](https://cloud.google.com/free)
    
-   [GCP Pricing Calculator](https://cloud.google.com/products/calculator?hl=en)
    
-   [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
    
-   [GKE Documentation](https://cloud.google.com/kubernetes-engine/docs)
    
-   [Cloud Storage Documentation](https://cloud.google.com/storage/docs)
    

----------

## **7. Next Steps**

-   Finalize required GCP services based on the project architecture.
    
-   Use GCP Pricing Calculator to finalize detailed cost estimates.
    
-   Set up billing alerts and budgets to control costs.
    
-   Document the infrastructure plan for future scaling.
    

