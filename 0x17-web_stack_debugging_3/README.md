
Web Stack Debugging #3

This project focuses on debugging a WordPress website running on a LAMP (Linux, Apache, MySQL, and PHP) stack. Debugging web stacks often requires going beyond traditional logging and diagnosing issues at various layers of the stack.


## Concepts

For this project, we expect to explore the following concepts:

Web Server
Web stack debugging
## Background Context

WordPress is a widely used tool for running blogs, portfolios, e-commerce, and company websites. It powers 26% of the web, making it highly likely that individuals will encounter it in their careers. WordPress typically runs on a LAMP stack, which consists of Linux, Apache, MySQL, and PHP.


## Requirements

All files will be interpreted on Ubuntu 14.04 LTS.
Files should end with a newline character.
A README.md file at the root of the project folder is mandatory.
Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
Puppet manifests must run without error.
Puppet manifests files must end with the extension .pp.
Files will be checked with Puppet v3.4.
More Info
Install puppet-lint:
bash
Copy code
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

## Setup

Ensure you have access to an Ubuntu 14.04 LTS system or set up a virtual machine or Docker container for testing purposes.

## Usage

Clone this repository to your Ubuntu 14.04 LTS system.
Write Puppet manifests to configure the LAMP stack.
Run puppet-lint to ensure manifests pass linting.
Apply Puppet manifests to set up and configure the LAMP stack.
Debug any issues encountered during the setup process.
## Authors

- [Julie Peters](https://github.com/Nimiabaga)

