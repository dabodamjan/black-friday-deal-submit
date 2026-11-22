# Test records for the check script

Bad records, one defect each, used by `python3 scripts/check-listings.py --self-test`.
`_expected.json` names the error each file must produce; `ok-pipe-in-name.json` is a
valid record whose name carries a pipe and a line break, to show the index writer
escapes them. None of these is a real list. The main script never reads this folder.
