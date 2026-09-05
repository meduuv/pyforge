# CLI Guidance

Command-line interfaces should keep successful output concise and failures actionable.

- Use stable exit codes for automation.
- Send human-readable diagnostics to stderr when appropriate.
- Keep examples copyable and safe to run.
- Document required arguments and defaults.
- Avoid exposing secrets or local filesystem details in error messages.
