# oc_p10_pur_beurre

Project #10 in OC Python course

Author: etienne86

## Purpose

Based on the [project #08](https://github.com/etienne86/oc_p08_pur_beurre), the purpose is here to deploy the web application on a server setup manually.

## Main features

The features added in this repository (versus [oc_p08_pur_beurre](https://github.com/etienne86/oc_p08_pur_beurre) are:
* push the changes on branch 'staging' to pass the Travis approval (if OK, then merge in branch 'master', 'git push origin master' on your machine, and 'git pull origin master' on the server)
* the server IP is 178.62.10.30 (hosted by DigitalOcean)
* logs are monitored with Sentry
* the products database is updated every week (every Wednesday at 01:00 am - UTC)

## How to run the program

Please click on the following [link](http://178.62.10.30/).

## Test report

The test report is available [here](https://github.com/etienne86/oc_p10-pur_beurre/blob/master/deliverables/P10_rapport_de_tests.pdf).