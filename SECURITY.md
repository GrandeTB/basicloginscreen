# Security Policy

## Scope

This repository is an **educational Tkinter display-name demo**, not an authentication product. It deliberately has no passwords, accounts, credential handling, persistence, networking, sessions, or authorization.

It must not be used to protect resources, collect credentials, or represent a real login/sign-in interface.

## Reporting a vulnerability

Please do **not** open a public issue containing passwords, API keys, access tokens, personal data, or proof-of-concept material that could expose a user.

Instead, report the concern privately to the repository owner through their GitHub profile contact method. Include:

- a concise description of the issue;
- steps to reproduce it without sensitive data;
- the affected file and revision, if known; and
- an assessment of potential impact.

The maintainer will acknowledge reports when able and coordinate a fix or disclosure timeline as appropriate for this small educational project.

## Secure-use expectations

- Never add password fields, credential collection, or credential storage to this demo.
- Never commit secrets, `.env` files, access tokens, or personal data.
- Use a maintained authentication provider or framework for real applications; do not extend this example into one.
