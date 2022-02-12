---
layout: post
title: How Import to an IAM Role into Cloudformation
tags: [AWS, IAM, Cloudformation]
---

This is a blog about importing an existing IAM Role into Cloudformation(CFN). An IAM Role is one of the [supported resource types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) that can be imported into CFN. The use case for doing this is that you may have resources that were created via the AWS Console, and you want to move them to version control.

## Summary

Here are the docs on how importing resources work in AWS: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-new-stack.html#resource-import-new-stack-cli

And here are the docs for an example of how to import a resource: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html

I created an example Github repo with working code that follows this process using the [boto3](https://aws.amazon.com/sdk-for-python/). Please refer to this repo for example templates on the process. There is also a Jupyter notebook with documentation on how the created CFN template and IAM Role resource in AWS are updated at different steps of the process: https://github.com/aaronlelevier/import-iam-to-cfn

At the end of this test, I tried deleting the Role via the CFN stack, and the Role in AWS was not deleted and had to be deleted outside of the CFN stack.
