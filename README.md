# pmenu

Like dmenu, but in the command line.

# Examples

Given a file `bookmarks.txt` with the following contents:

```
fsf.org
archlinux.com
bitcoin.org
```

The following prints out 'archlinux.com':

```
$ cat bookmarks.txt | pmenu
0. fsf.org
1. archlinux.com
2. bitcoin.org
choice:
```
At this point, it awaits input from the user.
This is useful to move the selection down the pipeline. For example:

```
cat bookmarks.txt | pmenu | xargs firefox
```

You can also pass a filename as an argument:

```
pmenu -f bookmarks.txt | xargs firefox
```

# Installing

```
git clone git@github.com:miguel-r-s/pmenu.git
cd pmenu
./install.sh
```

This creates a symlink from `~/.local/bin/` to the implementation of `pmenu` in this repo.

# Issues

If something doesn't work, report an issue on Github or send a pull request with a fix.
