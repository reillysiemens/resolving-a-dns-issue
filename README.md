# Resolving A DNS Issue

This repository contains all the scripts and data necessary to reproduce
my blog post on [resolving a DNS issue][resolving-a-dns-issue].

You'll need:
- [Zsh][zsh]
- [Python 3.6+][py36], [Pygal][pygal], and [pandas][pandas].
- [Graphviz][graphviz]

To run the HTTP test on your own network:

```bash
export ROUTER_IP=${YOUR_ROUTER_IP}
export ROUTER_HOSTNAME=${YOUR_ROUTER_HOSTNAME}
export OUTPUT_FILE="your-results.csv"
zsh http-test.zsh
```

To run the chart generation script:

```bash
python3.6 chart.py ${OUTPUT_FILE} ${OUTPUT_FILE%.csv}.svg
```

To find failure percentages:

```bash
zsh percent-failures.zsh
```

To generate the _It's Always DNS_ diagram:

```bash
dot -Tsvg its-always-dns.dot -o its-always-dns.svg
```

[resolving-a-dns-issue]: https://tuckersiemens.com/posts/resolving-a-dns-issue/
[zsh]: https://www.zsh.org/
[py36]: https://www.python.org/downloads/release/python-360/
[pygal]: http://pygal.org/en/stable/
[pandas]: https://pandas.pydata.org/
[graphviz]: https://www.graphviz.org/
