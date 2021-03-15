Table of Contents
-----------------

  * Building Software for the Cloud
    * Practice Quiz: Building Software for the Cloud <br>
        * `01_building_software_for_the_cloud.ipynb`
  * Monitoring & Alerting
    * Practice Quiz: Monitoring & Alerting <br>
        * `02_monitoring_and_alerting.ipynb` 
  * Troubleshooting & Debugging
    * Practice Quiz: Troubleshooting & Debugging <br>
        * `03_troubleshooting_and_debugging.ipynb`
  * Module Review
    * Qwiklabs Assessment: Debugging Cloud Deployment <br>

# Recap
## Storing Data in the Cloud
- Block storage in the Cloud acts almost exactly like a hard drive. The operating system of the virtual machine will create and manage a file system on top of the block storage just as if it were a physical drive. 
- Persistent storage is used for instances that are long lived, and need to keep data across reboots and upgrades. On the flip side, ephemeral storage is used for instances that are only temporary, and only need to keep local data while they're running. 
- If you're trying to deploy a Cloud app that needs to store application data, you'll probably need to look into other solutions like objects storage, which is also known as blob storage. Object storage lets you place in retrieve objects in a storage bucket. These objects are just generic files like photos or cat videos, encoded and stored on disk as binary data. These files are commonly called blobs, which comes from binary large object, and as we called out, these blobs are stored in locations known as buckets.
- Throughput is the amount of data that you can read and write in a given amount of time.
- IOPS or input/output operations per second measures how many reads or writes you can do in one second, no matter how much data you're accessing.
- Latency is the amount of time it takes to complete a read or write operation.
- Read latency is sometimes reported as the time it takes a storage system to start delivering data after a read request has been made, also known as time to first byte.
- Hot data is accessed frequently and stored in hot storage while cold data is accessed infrequently, and stored in cold storage.

## Load Balancing
- A pretty common load balancing technique is round robin DNS.
- Using sticky sessions means all requests from the same client always go to the same back end server. 
- Use Geo DNS and geoip. These are DNS configurations that will direct your clients to the closest geographical load balancer. The mechanism used to route the traffic relies on how the DNS servers respond to requests. 
- Content delivery networks or CDNs. They make up a network of physical hosts that are geographically located as close to the end user as possible.

## Change Management
- You can experiment using A/B testing. In A/B testing, some requests are served using one set of code and configuration, A, and other requests are served using a different set of of code and configuration, B.

## Understanding Limitations
- Utilization limits, which cap the total amount of a certain resource that you can provision.

## Getting Started with Monitoring
- Monitoring lets us look into the history and current status of a system. We'll check out a bunch of different metrics. 
- There's a bunch of different monitoring systems out there. Some systems like AWS Cloudwatch, Google Stack Driver, or Azure Metrics are offered directly by the Cloud providers. Other systems like Prometheus, Datadog, or Nagios can be used across vendors.
- Some systems use a pull model, which means that the monitoring infrastructure periodically queries our service to get the metrics. 
- When push monitoring is used, the service being monitored actively sends metrics to the monitoring system. 
- Pro tip, you only want to store the metrics that you care about, since storing all of these metrics in the system takes space, and storage space costs money. 
- Whitebox monitoring checks the behavior of the system from the inside.
- On the flip side, blackbox monitoring checks the behavior of the system from the outside. This is typically done by making a request to the service and then checking that the actual response matches the expected response.

## Getting Alerts When Things Go Wrong
- The most basic approach is to run a job periodically that checks the health of the system and sends out an email if the system isn't healthy.
- On a Linux system, we could do this using cron, which is the tool to schedule periodic jobs.
- Those that need immediate attention are called pages, which comes from a device called a pager.
- On the flip side, the non-urgent alerts are usually configured to create bugs or tickets for an IT specialist to take care of during their workday. They can also be configured to send email to specific mailing lists or send a message to a chat channel that will be seen by the people maintaining the service. 

## Service-Level Objectives
- SLOs are pre-established performance goals for a specific service. Setting these objectives helps manage the expectations of the service users, and the targets also guide the work of those responsible for keeping the service running. SLOs need to be measurable, which means that there should be metrics that track how the service is performing and let you check if it's meeting the objectives or not.
- A service level agreement is a commitment between a provider and a client.
- If we have an SLO of 99.99%, that gives us an error budget of .01%.

## Identifying Where the Failure Is Coming From
- If it fails in the other regions too, it's likely that it's a problem with your system.
- If you're seeing problems related to resource usage, you can try running the same system in a different machine type and checking how it behaves there. 
- Containers are packaged applications that are shipped together with their libraries and dependencies. Each application is executed in a separate container, completely independent of any other applications running on the same machine. 

## Recovering from Failure
- If you operate a service that stores any kind of data, it's critical that you implement automatic backups and that you periodically check that those backups are working correctly by performing restores.
- Many teams keep backup or a secondary instances of their services already up and running. That way, if there's a problem with the primary instance, they can simply point the load balancer or the DNS entries to the secondary instance with minimal disruption to the service. 
- Alternatively, it's common practice to have enough servers running at any time so that if one of them goes down, the others can still handle the traffic, or on a larger scale, have the service running on different data centers around the world, so that if one of the data centers has a problem, the service can still be provided by the instances running in the other data centers.