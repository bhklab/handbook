# Compute Engine

Compute Engine on GCP is the standard and most basic VM creation workflow (similar to EC2 on AWS or Virtual Machines on Azure). It is the most common way in the lab to deploy web applications and API's.

## Why Compute Engine

Despite how basic Compute Engine is, it is extremely important for the following reasons:

- Allows for full control.
	- Nginx configurations (allowing for many different projects to be routed to)
	- Certificate management for domains or sub domains
	- System services management (Ideal for many APIs)
- Available 24/7, no downtime or boot up time unless explicilty enforced
	- Unlike Cloud Run or Build where when the application becomes dormant, there will be boot up time upon requesting access to the resource (not ideal for API's or web-apps)
- Fairly cost effective. 
	- $25-35 CAD/month for a front-end and back-end deployment that will accessible 24/7
- Relatively easy to use if you're familiar with Linux/Unix systems


## Cost

Compute Engine VMs can really vary in cost. You usually need a basic N1 for a web application deployment (front-end+API). This tends to cost $25-35 CAD/month depending on how much SSD is needed on the VM to clone the project and host data if needed. However, with some very light workflows or beta/QA deployments you can get away with using a f1 micro or g1 small which will only cost around 10-15 CAD/month.
