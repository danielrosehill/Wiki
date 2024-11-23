---
title: "Hacky SaaS Export Archive Incremental Backup Script"
---

![alt text](../images/saas_export/backup-sloth2.png)

## Why backup SaaS data?

As a longtime dabbler in all manner of tech things, I've come to appreciate the huge value in keeping reliable backups of your data.

If you want my thoughts [at length](https://docs.bydanielrosehill.com/repos/blogs/thought-on-tech/backups/) about why I think that backing up *even* SaaS data is **really important**, click the preceding link (sorry, I'm being lazy today).

The TL;DR is that while I think that many SaaS tools are truly wonderful (PS: as a Linux user, I *try* to find SaaS-anything as it's a great way to work around cross-platform compatibility issues), I will never apologise for wanting to keep an independent copy of what I regard as important data. 

Nor will I ever fully trust a SaaS provider's insistence that *"we do backups, your data is safe."* It's my data and I don't want to forefeit ownership over it entirely just because your platform is truly great.

 ![alt text](../images/saas_export/sloth-backups.webp)

## The problem: SaaS doesn't give backup much love

Firstly, things aren't *all* that bleak.

There *are* SaaS providers (let's use Github as an example) that actually do a pretty great job at allowing users to have their cake and eat it too:

- You can use our great tech (which is probably way better than the self-hostable alternatives. Also, you don't need to host it!)  
- Here's an API that will allow you to do whatever you want with the data you're storing here.  

Thus, it's pretty easy, using Github, to do things like write Python scripts that will periodically duplicate your repositories onto, say, your NAS. 

To my mind, this should be the basic standard for shared data federacy in SaaS. Sadly it isn't. There are many tools I love but who only allow users to export their data as `zip` archives which invariably:

- Can't be used programatically  
- From a backup standpoint (if they can be considered backups at all) are very far from ideal. They're data-inefficient full backups which spit out the full user data *every single time* they run.   

With a bit of effort, though, you can implement a next-best-thing solution.

## V1 of my Zip archive approach

Here's an approach that I've developed using [Nuclino](https://www.nuclino.com) which offers excellent markdown handling.

The tool has a feature to export your workspace:

 ![alt text](../images/saas_export/export-workspace.png)

This gets you a `.zip`:

![alt text](../images/saas_export/zip.png)

Inside of this are individual files:

 ![alt text](../images/saas_export/files.png)