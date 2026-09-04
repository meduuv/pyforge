# Error handling

Library code should raise specific exceptions for invalid input and environmental failures.

Avoid exposing secrets or filesystem details in user-facing errors. CLI layers should convert expected exceptions into actionable messages and non-zero exit codes.
