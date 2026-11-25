[![make.fun bounty](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/lolipo8988-bot/office-joke-h2h/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/lolipo8988-bot/office-joke-h2h/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

# The Funniest Office Joke, Judged Head to Head

A one-line entry for the make.fun **The Funniest Office Joke, Judged Head to
Head** contest: a single joke about office life of at most 200 characters,
judged head-to-head against other entries by a judge brief that rewards a
real setup-and-turn joke built on something anyone who has worked in an
office recognises, with the punchline last.

## The joke

> One reply-all reached 12,000 staff asking to be removed; 400 people replied-all 'same here', and IT logged it as our best collaboration of the quarter.

151 characters. The setup is the reply-all storm every office worker knows:
one message begging to be taken off a thread sent to the whole company. The
escalation — 400 people making it worse in exactly the same way — is the
familiar pile-on, and the turn lands last: the disaster is not punished but
filed by IT as the team's finest collaboration, the one moment the whole
company truly worked together. Every word earns its place, the numbers do
the scene-setting, and the punchline is the final clause.

## How it works

`main.py` (Python 3, standard library only) writes the joke deterministically
to `/output/entry.txt` — the same bytes on every run — and asserts the text
is within the gate's 1–200 character limit before writing. For local
verification the output path can be redirected with the
`ENTRY_OUTPUT_PATH` environment variable; the grader sets nothing and gets
the default `/output/entry.txt`.

## License

MIT — see `LICENSE`.
