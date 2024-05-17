# Web Stack Debugging Project

## Overview
This project aims to debug and optimize a web stack featuring Nginx to handle high traffic without failing requests. The goal is to reduce the number of failed requests to zero under a load of 2000 requests with a concurrency level of 100.

## Requirements
- Ubuntu 14.04 LTS
- Puppet v3.4
- puppet-lint v2.1.1

## Installation
1. Install Ruby and puppet-lint:
   ```bash
   sudo apt-get install -y ruby
   sudo gem install puppet-lint -v 2.1.1

