---
layout: post
title: Android Meetup - A/B Test Experimentation/Feature flagging
tags: [A/B Testing, Feature Flagging, Android, Firebase]
---

![Imgur](https://i.imgur.com/OO5YuOX.png)

This blog post is about the Android Meetup that I went to where a Sr. Android Dev on the Uber Eats team discussed A/B Test Experimentation and Feature flagging

## A/B Test Experimentation, What is it?

It's testing two similar groups with different features to see which features are more popular / better

### why is this valuable

apps features are then driven by what customers want

because there if is a bug, the feature can be disabled vs. waiting for a new version of the app to be deployed and the User has to have on auto-update

auto-update - a lot of Users disable this and do manual app updating

can hide new feature behind a flag when it crashes

can flag based on an Android version

### How are features enabled / disabled

toggle feature flags on the server

### feature flag libraries

Morpheus - Uber

Ik - Facebook

their are open source libraries to do this

## Deployment statistics

### Android deploy

takes 30 minutes to role out a deploy

### iOS deploy

takes 1 week


### switches

geofences - like at the airport

devices

target by group

per app flavor

### merging code with flags

great because code gets merged that isn't running yet until the the flag is enabled

### FirebaseRemoteConfig

config on the server to toggle feature flags

FirebaseRemoteConfig is loaded on App boot, and then static calls to get data from the cache

### if / else pattern with feature flags

eliminate after sometime

Factory pattern to abstract if/else but if/else checks are just moved there

### when to launch experiment

don't experiment on new Users

wait for a User to be logged in

can't be the first time the app is started

- maybe the RemoteConfig callback comes later, and other experiments are being ran, so done on the 2nd bootup or later

### commits

message says

- how to test
	- this says turn on this flag
	- restart app
	- do this thing
- how to revert
	- this says to toggle the flag the other way

### Scaling

For servers - it's for traffic

For mobile - it's for developers

- number of developers
- as they leave
- processes

### merging code process at Uber

Lynting checks are run before committing

Espresso tests

Unit tests

No QA

## Testing

Abstract Activites

Dagger for Mocks

Try to not use Android as much as possible in the logic - better for testing

big device lab

- is international for testing
- can remotely connect to a device lab

### Uber

Don't use Gradle - they use Buck (created by Facebook)

Use a module system - there are 1000 modules

40m APK size

- obfuscated
- minified, etc...

Unobfuscated Debug version - 100m

- test code

Redex - for launching an app quickly

Obfuscation - use's Google Proguard

Anthing for $$ - is internally built

- b/c it can't be down

Lots of 3rd party libs

Open source as much as possible

Buck - is open source

OkHttp - contribute to this

### Architecture

MVC - is used, so Activity class is much smaller



### things to learn

webview

in app webview

### mockups

no testing via Invision mock ups

always testing on Users

## Firebase

Google Play services is needed

A/B testing exists out of the box in Firebase

- just has to be enabled
- Users will get collected into the A/B groups via the Firebase infrastructure

## Feature Flags

for new features

variants of current features

will get notified if a feature is a security vulnerability

### Locally changing of feature flags

can do this Locally, not on the main FirebaseRemoteConfig

### toggling flags

can do this programmatically after so many crashes

things to flag on

- city
- phone type
- Android version

### Build flavors

Only have 2 versions:

- debug
- prod

## Libraries

Charles - shows http calls

## A/B Test

has to be statistically significant

crashes

usage groups should be statistically significant

- groups should have similar profiles in order to be comparable. i.e same phone or Android version

PhD's evaluate if crashes are statistically significant and stats on feature usage to see what features should be used

Optimizely - library for measuring stats of usage

sample size - depends on the feature

### Java version

version is 8 in the demo

# other notes

take advantage of new features

### Editor Config

show param names for methods (currently I have this turned off)

### Locations

wifi trusted locations exists in Android O

### code

Dagger - to initialize dependency graph

retrofit

RxJava



