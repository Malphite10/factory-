# Recovery Rules

Rules for handling agent failures and QA rejects.

1. **QA Fail**: If a template fails QA, route back to the Production Agent with the QA Report.
2. **Security Block**: If a dependency is flagged, route to the Supply Chain Gatekeeper for resolution.
3. **Model Timeout**: Retry with a fallback model defined in model-routing.
