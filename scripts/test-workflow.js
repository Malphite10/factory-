const fs = require('fs');
const path = require('path');
const Ajv = require('ajv');
const addFormats = require('ajv-formats');

const ajv = new Ajv({ allErrors: true });
addFormats(ajv);

console.log('--- Workflow Test Simulator ---');

const mockHandoff = {
  agent: "03-design",
  version: "1.0.0",
  timestamp: new Date().toISOString(),
  inputs: {
    product_spec: {},
    design_system_version: "1.2.0"
  },
  tasks: ["Create Figma mockups", "Define color palette"],
  outputs: {
    figma_url: "https://figma.com/file/123",
    design_tokens: {},
    component_inventory: [],
    responsive_breakpoints: {}
  },
  handoff: {
    next_agent: "05-github-supply-chain",
    design_system_compliance: true
  },
  blockers: []
};

const schema = JSON.parse(fs.readFileSync(path.join(__dirname, '../agents/schemas/design-package.json'), 'utf8'));
const validate = ajv.compile(schema);
const valid = validate(mockHandoff);

if (valid) {
  console.log('✓ Handoff package valid for 03-design');
} else {
  console.error('✗ Handoff package INVALID:', validate.errors);
  process.exit(1);
}

console.log('--- Simulator Complete ---');
