# Testing Guidance

Tests should cover the public behavior users depend on rather than implementation details.

## Recommended coverage

- Valid inputs and expected outputs
- Boundary values
- Invalid inputs and documented exceptions
- CLI behavior when applicable
- Regression cases for fixed bugs

Keep tests deterministic and independent from external services unless an integration test explicitly requires one.
