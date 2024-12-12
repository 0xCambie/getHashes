# getHashes
Simplistic Python CLI Tool to generate hashes from a file, list of files or directory with malware samples.

To use this tool, simply target the directory with all the malware samples that need to get hashed:

```bash
./getHashes.py -d /path/to/directory/ -o output
```

If you want the hashes for only one file:
```bash
./getHashes.py -f /path/to/the/file.malz -o output
```

If you needd hashes for samples that are in a list file, we can run:
```bash
./getHashes.py -l /path/to/the/list
```
