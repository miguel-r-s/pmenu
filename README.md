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
cat bookmarks.txt | pmenu
```

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
./install.sh
```
