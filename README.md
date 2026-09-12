# Educational Tkinter Display-Name Demo

A small, runnable Python project that demonstrates a Tkinter form, simple display-name validation, and message-box feedback.

> **Not authentication software.** This project does not implement login, user accounts, passwords, credential storage, sessions, encryption, authorization, or access control. It asks only for a temporary display name and must not be adapted or presented as a real sign-in flow.

## Requirements

- Python 3.10 or later (the code uses modern `str | None` type syntax)
- Tkinter, which is included with most standard Python installations

No third-party packages are required.

## Run the demo

From the repository root:

```bash
python basicloginscreen.py
```

Enter a non-blank display name and choose **Continue to demo**. The name is only used in the in-memory welcome message; it is not saved or transmitted.

If your environment does not provide a graphical display, do not run the GUI. You can still run the tests and import smoke check below.

## Run checks

The test suite is deliberately non-interactive and does not open a Tkinter window:

```bash
python -m unittest discover -s tests -v
python -m compileall -q basicloginscreen.py demo_access.py tests
python -c "import basicloginscreen, demo_access; print('import smoke check passed')"
```

## What this demonstrates

- Tkinter labels, text entries, buttons, and grid layout
- Rejecting blank display-name input
- User feedback through message boxes
- Keeping validation logic separate from the GUI so it can be unit-tested

## Project layout

- `basicloginscreen.py` — GUI entry point
- `demo_access.py` — display-name validation helper
- `tests/` — non-interactive unit tests

## Security

Please see [SECURITY.md](SECURITY.md). Do not submit credentials, tokens, or other secrets through this demo or in issue reports.
