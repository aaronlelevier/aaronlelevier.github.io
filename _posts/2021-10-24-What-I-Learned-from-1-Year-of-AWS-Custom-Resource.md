---
layout: post
title: What I Learned from 1 Year of AWS Custom Resource
tags: [AWS, AWS Custom Resource]
---

The title of this article could have also been, *"Using AWS Custom Resource's."* or maybe *"AWS Custom Resource Gotchas and how to avoid them."*   Either way, the goal of this article is to talk about usage and gotchas. With that said, this article is meant to be in addition to the AWS Official Documentation, linked below the [References](#References). I will highlight a few important aspects of AWS Custom Resources with the way that they work.

## What is an ACR

An AWS Custom Resource<sub>1</sub> (ACR) is a mechanism in AWS Cloudformation (CFN) that allows an arbitray payload to be sent to a compute function.  

There are two ACR types:

- AWS Lambda - sync - must always return a response (pass or fail)
- AWS SQS Queue - async

This article covers AWS Lambda as this is the common case.

ACRs have a  Request<sub>2</sub> and Response<sub>3</sub> structure.

## The first thing you learn

The first major lesson of AWS Lambda ACRs is that they must always return a Response. If an ACR errors and fails to send a Response, the CloudFormation (CFN) parent stack invoking the ACR will spin for 1 hour, and eventually timeout, and fail.

## How to always send a Response

In order to achieve always sending a Response, you should wrap the invocation of your code in a top level `try/catch` where all errors be caught and send a ACR Response of `fail`

You could wrap your code in the following:

```java
try:
  f(event)
  success
catch:
  fail
```

### Success case

In the success case, ACR Response data can be returned, which can be an arbitrary single level `key/value` map.

This data is then referenceable using the CFN intrisic function: ``Fn::Getatt`<sub>8</sub>

### Fail case

In the failure case, an Error Reason and Error Message can be sent.

This will result in a ROLLBACK by your parent CFN stack.

## ACR Request 

An ACR Request consists of the ACR endpoint, e.g. the AWS Lambda ARN, optional key/value arguments, and metadata.

### The Lambda ARN

This payload will be sent as an Event to the Lambda ARN.

### Optional Key/Value arguments

These arguments will appear as top level key/value arguments in the `ResourceProperties` section of the Lambda Event.

The value of these arguments can be a nested data structure.

### Metadata

AWS metadata is also sent in the ACR Request. This will include the parent CFN Stack Id, PhysicalResourceId, and so on.

### The PhysicalResourceId

This value can be updated in order to trigger certain desired behavior.  First CFN will process a RequestType of UPDATE, based on the **new** `PhysicalResourceId` in the Event. Then CFN sends an Event with a RequestType of DELETE with the **old** `PhysicalResourceId` and previous Event. This is sent after the UPDATE has succeded during the `UPDATE_COMPLETE_CLEANUP_IN_PROGRESS` phase.

## ACR RequestType

There are 3 request types, and these match based on what the parent CFN stack is doing:

- CREATE
- UPDATE
- DELETE

## Deploy it

An ACR, like any other AWS Resource can be deployed with CFN<sub>4</sub>, AWS SAM<sub>5</sub>, or some other deployment method.

### Replace an ACR

An ACR can NOT be replaced via tearing down and rebuilding if it is referenced in another CFN Stack, regardless of referencing the ACR directly or as  variable using an SSM Parameter<sub>9</sub> or CFN ImportValue<sub>10</sub>. You must solve for this.

## Finally

Okay, now that I know everything about ACRs, can I go write some code?

Yes!

Thank you.


## References

[1] - [AWS Custom Resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html)

[2] - [AWS Custom resource request objects](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requests.html)

[3] - [AWS Custom resource response objects](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-responses.html)

[4]  - [AWS::CloudFormation::CustomResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html)

[5] - [AWS Serverless Application Model (SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html)

[6] - [AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html)

[7] - [AWS::Lambda::LayerVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html)

[8] - [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html)

[9] - [AWS::SSM::Parameter](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html)

[10] - [Fn::ImportValue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html)
