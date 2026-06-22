# Template Validation Skill

## Required Checks
- **Responsive**: Mobile, Tablet, Desktop
- **Accessibility**: Contrast, Heading hierarchy, Keyboard navigation, Alt text
- **Performance**: Asset optimization, Unused assets, Layout shifts
- **CMS**: Collection connections, Dynamic pages, Empty state handling
- **Forms**: Submission success, Validation errors, Email triggers
- **SEO**: Title tags, Meta descriptions, Open Graph, Structured data

## Output
```json
{
  "status": "approved",
  "critical_issues": [],
  "warnings": [],
  "passed_tests": [],
  "score": 0,
  "next_agent": "launch-agent"
}
```

## Reject if:
- Critical issue exists.
- Broken navigation exists.
- CMS is disconnected.
- Accessibility score fails.
