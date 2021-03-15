Table of Contents
-----------------

  * Cloud Computing
    * Practice Quiz: Cloud Computing <br>
        * `01_cloud_computing.ipynb`
  * Managing Instances in the Cloud
    * Practice Quiz: Managing Instances in the Cloud <br>
        * `02_managing_instances_in_the_cloud.ipynb` 
  * Automating Cloud Deployments
    * Practice Quiz: Automating Cloud Deployments <br>
        * `03_automating_cloud_deployments.ipynb`
  * Module Review
    * Qwiklabs Assessment: Create VM template and Automate deployment <br>

# Recap
## Cloud Services Overview
- Software as a Service or SaaS, is when a Cloud provider delivers an entire application or program to the customer.
- Platform as a Service or PaaS, is when a Cloud provider offers a preconfigured platform to the customer.
- Infrastructure as a Service or IaaS, is when a Cloud provider supplies only the bare-bones computing experience. 

## Scaling in the Cloud
- In particular, we call it upscaling when we increase our capacity and downscaling when we decrease it. 
- To scale a deployment horizontally, we add more nodes into the pool that's part of a specific service. You add more servers to increase your capacity. If the traffic goes up you could just add more servers to keep up with it.
- On the flip side, if you're scaling a deployment vertically, it means you're making your nodes bigger. When we say bigger here we're talking about the resources assigned to the nodes like memories, CPU, and disk space.
- When we set our service to use automatic scaling, we're using a service offered by the Cloud provider. This service uses metrics to automatically increase or decrease the capacity of the system.
- On the flip side, using manual scaling means that changes are controlled by humans instead of software.

## Migrating to the Cloud
- IaaS is especially useful to administrators using a lift and shift strategy. 
- Containers are applications that are packaged together with their configuration and dependencies. This allows the applications to run in the same way no matter the environment used to run them. 

## Templating a Customized VM
- Using gcloud cli:

  ```bash
  # First init and login
  $ gcloud init

  # Create 5 additional VM
  $ gcloud compute instances create --source-instance-template webserver-template ws1 ws2 ws3 ws4 ws5
  ```

## Cloud Scale Deployments
- A load balancer ensures that each node receives a balanced number of requests.
- Autoscaling allows the service to increase or reduce capacity as needed while the service owner only pays for the cost of the machines that are in use at any given time.

## What is orchestration?
- Orchestration is the automated configuration and coordination of complex IT systems and services. In other words, orchestration means automating a lot of different things that need to talk to each other. 
- By using orchestration tools, we can automate the configuration of any monitoring rules that we need to set, which metrics we want to look for, when we want to be alerted, and so on, and automatically apply these to a complete deployment no matter which datacenter the services are running in.

## Cloud Infrastructure as Code
- Storing our infrastructure in a code like format, lets us create repeatable infrastructure, and that using Version control for the storage, means that we can keep a history of what we've done and easily rollback mistakes.
- Amazon has Cloud Formation, Google has Cloud Deployment Manager, Microsoft has Azure Resource Manager, and OpenStack has Heat Orchestration Templates. These tools are specific to the Cloud provider, which means it can be complex and cumbersome to move to a different provider or combine a Cloud deployment with an on-premise deployments.
- An option that's becoming really popular in the Orchestration field, is called Terraform. Similar to Puppet, Terraform uses its own Domain-specific language which lets us specify what we want our Cloud infrastructure to look like. The cool thing about Terraform is that it knows how to interact with a lot of different Cloud providers and automation vendors.