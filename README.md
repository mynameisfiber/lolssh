# lolssh

> Because I want to lol on *all* of my commits

This is a hacked together set of tools so that you can lolcommit even when
working with remote machines.  BE WARNED: this is a hack.

## Install

### Git Hook

Install the `post_commit` hook into your git templates.  You can replace the
default lolcommits post_commit code with the provided one.  If you don't know
what I mean by a git template, go to the [lolcommits
tutorial](https://github.com/mroth/lolcommits/wiki/Enabling-Lolcommits-for-all-your-Git-Repositories)
on the issue and instead of copying their hook, copy mine... it's better, I
swear.

NOTE: you'll have to `git init` any repos you want to lolcommit on after
installing the new hook.  This will simply make sure the repo has the updated
hooks as given by your git templates.

### SSH Tunnel

Now, we want a way for any server you connect to to be able to speak to your
client computer.  This can be done by doing a reverse tunnel.  Edit your ssh
config file (`~/.ssh/config`) and add the following,

```
Host *
    RemoteForward 17363 127.0.0.1:17363
```

Note that this enables the forwarding on ALL machines.  You may want to be a bit
more specific and only enable this forwarding on machines you will be committing
on.

### lolcommits server

Finally, run the `lolcommits_server.py` process and profit!  You'll want this
running any time that you are going to be doing remote commits.

## Future

Make the install automated!
