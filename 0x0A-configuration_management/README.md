Puppet Configuration Management Project
Overview
This project aims to implement Puppet configuration management for automating infrastructure provisioning, configuration, and maintenance. Puppet will help ensure consistency across servers and reduce the risk of incidents similar to the one experienced with the Skynet auto-remediation tool at SlideShare.

Background Context
During my time at SlideShare, I encountered an incident where a bug in the auto-remediation tool caused significant disruption to the infrastructure. Thanks to Puppet, we were able to restore normal operation swiftly, highlighting the importance of configuration management in maintaining a stable and reliable infrastructure.

Resources
Intro to Configuration Management
Puppet resource type: file
Puppet’s Declarative Language: Modeling Instead of Scripting
Puppet lint
Puppet emacs mode
Requirements
General
Ubuntu 20.04 LTS VM with Puppet 5.5 preinstalled
Puppet manifests must pass puppet-lint version 2.1.1 without any errors
Puppet manifests must run without error
Puppet manifests files must end with the extension .pp
Note on Versioning
Do not attempt to upgrade versions; stick to the provided Puppet 5.5 version for this project.
Installation
bash
Copy code
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
$ gem install puppet-lint
Project Structure
manifests/: Directory to store Puppet manifest files (.pp extension).
README.md: Documentation for the project.
Usage
Clone this repository to your Ubuntu 20.04 LTS VM.
Navigate to the project directory.
Write your Puppet manifests in the manifests/ directory.
Test your Puppet manifests using puppet-lint and ensure they run without errors.
Implement Puppet configuration management based on the project requirements and guidelines.
Contributing
Contributions to improve this project are welcome! If you have suggestions or find any issues, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Julie Peters - Contact: nimi@abaga@yahoo.com


