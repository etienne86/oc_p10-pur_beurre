# oc_p10-pur_beurre

Project #10 in OC Python course

Author: etienne86

## Purpose

Based on the [project #08](https://github.com/etienne86/oc_p08_pur_beurre), the purpose is to deploy the web application on a server setup manually.

## Main features

The features added in this repository (versus [oc_p08_pur_beurre](https://github.com/etienne86/oc_p08_pur_beurre)) are:
* from your machine, push the changes on branch 'staging' to pass the Travis approval - if OK:
    * git checkout master
    * git merge staging
    * git push origin master
    * git checkout staging
* if the previous steps are performed and OK, pull the changes on the server: git pull origin master
* the server IP is 178.62.10.30 (hosted by DigitalOcean)
* logs are monitored with Sentry
* the products database is updated every week (every Wednesday at 01:00 am - UTC)

## How to run the program

Please click on the following [link](http://178.62.10.30/).

## Test report

The test report is available [here](https://github.com/etienne86/oc_p10-pur_beurre/blob/master/deliverables/P10_rapport_de_tests.pdf).