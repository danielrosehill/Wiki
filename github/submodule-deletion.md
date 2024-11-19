---
title: "Dirty flags for submodules"
og_title: "Dirty flags to prevent Github Catastrophes"
og_image: "https://docs.bydanielrosehill.com/repos/wiki/images/horrified-cat.webp"
---

# Adding 'dirty' flags to prevent Github submodule conflict hell

![alt text](../images/horrified-cat.webp)

## The problem:

While Github submodules are amazing (especially for presenting multiple documentation repositories as one) they come with some potential perils.

One of those is that it's *really* easy to do the following:

- Add submodules to your main repo  
- Accidentally create file(s) in the submodules

The fix is standard Github conflict resolution. 

But if you've got better things to do than go hunting errant commits, you can get ahead of the game by adding 

`ignore=dirty`

to your submodules as set out in `.gitmodules`

According to these [docs](https://git-scm.com/docs/git-status/2.11.4#:~:text=Using%20%22dirty%22%20ignores%20all%20changes,when%20the%20config%20option%20status.)

> Ignore changes to submodules when looking for changes. <when> can be either "none", "untracked", "dirty" or "all", which is the default. Using "none" will consider the submodule modified when it either contains untracked or modified files or its HEAD differs from the commit recorded in the superproject and can be used to override any settings of the ignore option in git-config[1] or gitmodules[5]. When "untracked" is used submodules are not considered dirty when they only contain untracked content (but they are still scanned for modified content). Using "dirty" ignores all changes to the work tree of submodules, only changes to the commits stored in the superproject are shown (this was the behavior before 1.7.0). Using "all" hides all changes to submodules (and suppresses the output of submodule summaries when the config option

# Code Snippet

```
[submodule "site-base/docs/repos/prompt-library"]
	path = site-base/docs/repos/llms-and-ai/prompt-library
	url = https://github.com/danielrosehill/Prompt-Library
	ignore = dirty

[submodule "site-base/docs/repos/llms-on-llms"]
	path = site-base/docs/repos/llms-and-ai/llms-on-llms
	url = https://github.com/danielrosehill/LLMs-on-LLMs.git
	ignore = dirty

[submodule "site-base/docs/thought-on-tech"]
	path = site-base/docs/repos/thoughts-on-tech
	url = https://github.com/danielrosehill/My-Thoughts-On-Tech
	ignore = dirty

[submodule "docs/repos"]
	path = site-base/docs/repos/wiki
	url = https://github.com/danielrosehill/Wiki
	ignore = dirty

[submodule "site-base/repos/gvfd-deriv"]
	path = site-base/docs/repos/data-projects/gvfd
	url = https://github.com/danielrosehill/GVFD-Derivative-Docs
	ignore = dirty
```