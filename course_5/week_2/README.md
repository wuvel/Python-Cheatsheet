Table of Contents
-----------------

  * Deploying Puppet Locally
    * Practice Quiz: Deploying Puppet Locally <br>
        * `01_deploying_puppet_locally.ipynb`
  * Deploying Puppet to Clients
    * Practice Quiz: Deploying Puppet to Clients <br>
        * `02_deploying_puppet_to_clients.ipynb` 
  * Updating Deployments
    * Practice Quiz: Updating Deployments <br>
        * `03_updating_deployments.ipynb`
  * Module Review
    * Qwiklabs Assessment: Deployment Using Puppet <br>

# Recap
## Applying Rules Locally
- Installing Puppet package:

    ```bash
    $ sudo apt install puppet-master
    ```
- Create manifest with extension `.pp`.

    ```bash
    package { 'htop':
        ensure => present
    }
    ```
- Applying rules:

    ```bash
    $ sudo puppet apply -v tools.pp
    ```
    After loading all facts for a computer, the server calculates which rules actually need to be applied. The catalog is the list of rules that are generated for one specific computer once the server has evaluated all variables, conditionals, and functions. In this example, the catalog will be exactly the same as our code because the code didn't include any variables, functions, or conditionals. 

## Managing Resource Relationships
- You're not going to configure a package that's not installed and you don't want to start a service until both the package and the configuration are in place. Puppets lets us control this with resource relationships.
    - Example:

        ```bash
        class ntp {
            package { 'ntp':
                ensure => latest,
            }
            file { '/etc/ntp.conf':
                source => '/home/user/ntp.conf',
                replace => true,
                require => Package['ntp'],
                notify => Service['ntp'],
            }
            service {
                enable => true,
                ensure => running,
                require => File['/etc/ntp.conf'],
            }
        }

        include ntp
        ```
        We write resource types in lowercase when declaring them, but capitalize them when referring to them from another resource's attributes. At the bottom of the file, we have a call to include NTP. That's why we told Puppet that we want to apply the rules described in a class. 

## Organizing Your Puppet Modules
- In puppet, we organize our manifests into modules. A module is a collection of manifests and associated data. We can put any resource we want into a module, but to keep our configuration management organized, we'll group things together under a sensible topic.
- All manifests gets stored in a directory called manifests. The rest of the data is stored in different directories depending on what it does. The files directory includes files that are copied into the client machines without any changes, like the `ntp.conf`. The template's directory includes files that are preprocessed before they've been copied into the client machines. 
- Example using modules:

    ```bash
    $ tree modules/
    modules/
        ntp
            files
                ntp.conf
            manifests
                init.pp
    ```
- Install Apache modules:

    ```bash
    $ sudo apt install puppet-module-puppetlabs-apache
    ```
- As we called out, this manifest is special. It needs to always be present because it's the first one that's read by puppet when a module gets included. 
- Including global module:

    ```bash
    include ::apache
    ```

# Puppet Nodes
- Another way to apply different rules to different systems is to use separate node definitions. In Puppet terminology, a node is any system where we can run a Puppet agent. It could be a physical workstation, a server, a virtual machine, or even a network router, as long as it has a Puppet agent and can apply the given rules. 
- Example:

    ```bash
    # Default node
    node default {
        class { 'sudo': }
        class { 'ntp': 
            servers => ['ntp1.example.com', 'ntp2.example.com']
        }
    }

    # For Other node
    node webserver.example.com {
        class { 'sudo': }
        class { 'ntp': 
            servers => ['ntp1.example.com', 'ntp2.example.com']
        }
        class { 'apache': }
    }
    ```
- The node definitions are typically stored in a file called site.pp, which isn't part of any module. Instead, it just defines what classes will be included for what nodes. 

## Puppet's Certificate Infrastructure
- Puppet uses public key infrastructure, or PKI, to establish secure connections between the server and the clients. The one used by Puppet is secure sockets layer or SSL. The clients use this infrastructure to check the server's identity, and the server uses it to check the client's identity, and all communication is done over an encrypted channel that uses these identities so it can't be intercepted by other parties. 
- The CA (certificate authority) verifies the identity of the machine and then creates a certificate stating that the public key goes with that machine. After that, other machines can rely on that certificate to know that they can trust the public key, since it means the machine's identity has been verified.

## Setting up Puppet Clients and Servers
- Scenario:

    ```bash
    # Set autosign
    $ sudo puppet config --section master master set autosign true

    # SSH 
    $ ssh webserver

    # Install puppet
    ubuntu@ubuntu: $ sudo apt install puppet

    # Set the client
    ubuntu@ubuntu: $ sudo puppet config set server ubuntu.example.com

    # Run 
    ubuntu@ubuntu: $ sudo puppet agent -v --test

    # Edit node
    $ vim /etc/puppet/code/environments/production/manifests/site.pp

    ## Content:
    node webserver.example.com {
        class { 'apache': }
    }

    node default {}

    # Run again
    ubuntu@ubuntu: $ sudo puppet agent -v --test

    # Make Puppet run automatically
    $ sudo systemctl enable puppet
    $ sudo systemctl start puppet
    ```

## Modifying and Testing Manifests
- Use the puppet parser validate command that checks that the syntax of the manifests is correct on top of that we can also run the rules using the `--noop` parameter the name comes from no operations and it makes puppet simulate what it would do without actually doing it. 
- Puppet also lets us test our manifests automatically by using R-Spec tests in these tests. We can set the facts involved different values and check that the catalog ends up stating what we wanted it to.

## Safely Rolling out Changes and Validating Them
- In an infrastructure context, production is the parts of the infrastructure where a service is executed and served to its users. If you host a website, the servers that deliver the website content to the users are the production servers.
- So how can we roll out changes safely? The key is to always run them through a test environment first. The test environment should have one or more machines running the exact same configuration as the production environment. 
- So instead of pushing the changes to all nodes, we usually do it in batches. You could have some machines with the fact that marks them as early adopters or canaries.