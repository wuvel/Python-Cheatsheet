Table of Contents
-----------------

  * Automation at Scale
    * Practice Quiz: Automation at Scale <br>
        * `01_automation_at_scale.ipynb`
  * Introduction to Puppet
    * Practice Quiz: Introduction to Puppet <br>
        * `02_introduction_to_puppet.ipynb` 
  * The Building Blocks of Configuration Management
    * Practice Quiz: The Building Blocks of Configuration Management <br>
        * `03_the_building_blocks_of_configuration_management.ipynb`
  * Module Review
    * Qwiklabs Assessment: Debugging Puppet Installation <br>

# Recap
## What is scale?
- Being able to scale what we do means that we can keep achieving larger impacts with the same amount of effort.
- In short, a scalable system is a flexible one.
- Automation is an essential tool for keeping up with the infrastructure needs of a growing business. By using the right automation tools, we can get a lot more done in the same amount of time.

## What is configuration management?
- By manually deploying the installation and configuring the computer, we see that we're using **unmanaged configuration**.
- Using a configuration management system to handle all of the configuration of the devices in your fleet, also known as nodes. 
- There are lots of configuration management systems available in the IT industry today. Some popular systems include Puppet, Chef, Ansible, and CFEngine. 
- When we use a configuration management system, we write rules that describe how the computers in our fleet should be configured. These rules are then executed by the automation, to make the computers match our desired state. 

## What is infrastructure as code?
- We're using Infrastructure as Code when all of the configuration necessary to deploy and manage a node in the infrastructure is stored in version control.  This is then combined with automatic tooling to actually get the nodes provisioned and managed. 
- Machines are treated as replaceable resources that can be deployed on-demand through the automation.
- Having your infrastructure stored as code means that you can automatically deploy your infrastructure with very little overhead. If you need to move it to a different location, it can be deployed, de-provisioned, and redeployed at scale in a different locale with minimal code level changes. 
- Managing your Infrastructure as Code it means that your fleet of nodes are consistent, versioned, reliable, and repeatable.

## What is Puppet?
- We typically deploy puppet using a client-server architecture. The client is known as the Puppet agent, and the service is known as the Puppet master. When using this model, the agent connects to the master and sends a bunch of facts that describe the computer to the master. The master then processes this information, generates the list of rules that need to be applied on the device, and sends this list back to the agent. The agent is then in charge of making any necessary changes on the computer.

## Puppet Resources
- In puppet, resources are the basic unit for modeling the configuration that we want to manage. In other words, each resource specifies one configuration that we're trying to manage, like a service, a package, or a file.
  - Example of resource:

    ```bash
    class sysctl {
      # Make sure directory exists
      file { '/etc/sysctl.d':
        ensure => directory
      }
    }
    ```
    file -> resource. The puppet agent then turns the desired state into reality using providers. When the puppet agent processes a resource, it first decides which provider it needs to use, then passes along the attributes that we configured in the resource to that provider.

## Puppet Classes
- Example:

  ```bash
  class ntp {
    package { 'ntp':
      ensure => latest,
    }
    file { 'etc/ntp.conf':
      source => 'puppet://modules/ntp/ntp.conf'
      replace => true,
    }
    service { 'ntp':
      enable => true
      ensure => running,
    }
  }
  ```
   It makes sense to use this technique whenever we want to group related resources. 
- By grouping related resources together, we can more easily understand the configuration and make changes in the future.

## What are domain-specific languages?
- We can do much more complex operations using Puppet's domain specific language or DSL. 
- A domain specific language is a programming language that's more limited in scope. 
- Puppet facts. Facts are variables that represent the characteristics of the system.
- When the Puppet agent runs, it calls a program called factor which analyzes the current system, storing the information it gathers in these facts. Once it's done, it sends the values for these facts to the server, which uses them to calculate the rules that should be applied.
- Example Puppet DSL Facts:

  ```bash
  if $facts['is_virtual'] {
    package { 'smartmontools':
      ensure => purged,
    }
  } else {
    package { 'smartmontools':
      ensure => installed,
    }
  }
  ```

## The Driving Principles of Configuration Management
- Puppet uses a declarative language because we declare the state that we want to achieve rather than the steps to get there. 
- Another important aspect of configuration management is that operations should be idempotent. In this context, an idempotent action can be performed over and over again without changing the system after the first time the action was performed, and with no unintended side effects. 
- Using exec is not indepontent, but we can use this instead:

  ```bash
  exect { 'move example file':
    command => 'mv /home/user/example.txt /home/user/Desktop',
    # This means that the file will be moved if it exists and nothing will happen if it doesn't. 
    onlyif => 'test -e /home/user/example.txt',
  }
  ```
  Another important aspect of how configuration management works is the test and repair paradigm. This means that actions are taken only when they are necessary to achieve a goal. Puppet will first test to see if the resource being managed like a file or a package, actually needs to be modified. If the file exists in the place we want it to, no action needs to be taken. If a package is already installed, there's no need to install it again.

- Finally, another important characteristic is that Puppet is stateless, this means that there's no state being kept between runs of the agent. 

