#!/bin/sh

## Generate staging pipeline json
python ./generate-pipeline.py ${1} staging ./templates/template-staging-pipeline.json ./generated/${1}-staging-pipeline.json

## Generate production pipeline json
python ./generate-pipeline.py ${1} production ./templates/template-production-pipeline.json ./generated/${1}-production-pipeline.json

## Deploy application
./spin --config ./spinconfig application save --application-name showks-canvas-${1} --owner-email showks-containerdaysjp@gmail.com --cloud-providers kubernetes

## Deploy staging pipeline
./spin --config ./spinconfig pipeline save --file ./generated/${1}-staging-pipeline.json

## Deploy production pipeline
./spin --config ./spinconfig pipeline save --file ./generated/${1}-production-pipeline.json
