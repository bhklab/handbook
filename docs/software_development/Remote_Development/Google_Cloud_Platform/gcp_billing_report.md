# Monthly Reports from GCP Project

## **1. Overview**

This document explains how to **generate monthly billing reports** from **Google Cloud Platform (GCP)**.  
These reports help us track **cloud costs per service**, **resource usage trends**, and **budget planning** for the AIRCHECK project.

The final output will include:

-   **Monthly cost summaries**
    
-   **Per-service cost breakdown**
    
-   **Visualizations** of spending trends
    
-   Insights for the **monthly meeting**
    
----------

## **2. Prerequisites**

Before you start, make sure you have:

-   **GCP account access** with **Billing Admin** or **Viewer** role
    
-   Access to the **GCP Billing Account**
 
----------

### **Step 1 — Open the Billing Reports Page**

1.  Go to **GCP Console**
    
2.  Click the **menu (☰)** in the top-left corner.
    
3.  Select **Billing** → **Reports**.
    

----------

### **Step 2 — Select Time Range**

-   Choose **Current Month** to see **this month’s costs** so far.
    
-   Choose **Previous Month** to compare against last month.
    
-   You can also select **Custom Range** to analyze any specific period.
    

----------

### **Step 3 — Group Costs by Service and SKU**

In the **Billing Reports** page, there’s a **“Group By”** dropdown.  
Select:

-   **Service** → Shows costs per GCP product, e.g., Vertex AI, BigQuery, GCS, Dataproc, Cloud Run, etc.
    
-   **SKU** → Shows costs at a **more detailed level**, like:
    
    -   “Cloud Storage (Standard Storage  Regional, Long-Term Physical Storage)”
        
    -   “BigQuery Storage (per GB)”
        
    -   “Compute Engine (N2 Instance Core for region(s), E2 Instance Core for region(s) ”
        

You can also **combine** grouping:

-   **Group by Service + SKU** → Gives both the **high-level service** and its **detailed cost components**.
    

----------

### **Step 4 — Understanding What You See**

When you group **by Service**:

-   You’ll see **total costs per GCP service**
    
    -   Example:
        
        -   Vertex AI → **$200**
            
        -   BigQuery → **$75**
            
        -   GCS → **$40**
            

When you group **by SKU**:

-   You’ll see **specific resource costs** within a service
    
    -   Example (Vertex AI):
        
        -   Training hours → **$150**
            
        -   Prediction requests → **$50**
            

When you **group by Service + SKU**:

-   You’ll see a **hierarchical view**:
    
    `Vertex AI → Training vCPUs → $150 → Prediction API Requests → $50 BigQuery  → Active Storage → $40 → Query Processing → $35` 
    

----------


### **Step 5 — Download the Report**

You can export the billing report directly:

-   Click **Download CSV**
    
-   Choose **Current Month** or **Previous Month**
    