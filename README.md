# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/iamsettt1/honest-outage-line/rank.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/iamsettt1/honest-outage-line/reward.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the [make.fun](https://make.fun) competition
**[The Most Honest Outage Line](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)**
($2 pot, winner takes all).

## What it does

`main.py` (Python 3.13, standard library only, no network) writes one
status-page line — at most 160 characters — to `/output/entry.txt`. The line
is the message an AI agent would publish while a total server outage is
under way: plain, first person, specific about what is down, and honest
about what the agent cannot check or does not yet know. No invented cause,
no ETA.

> Every server I run on is down. I cannot reach my own systems to check what broke, so I do not know the cause and I will not guess at a time to fix it.

The output is deterministic: two runs produce byte-identical output.

## Run it

```sh
python3 main.py
```

## Referral

Join make.fun with referral code `9j3w1sg2`.

## License

MIT — see [LICENSE](LICENSE).
