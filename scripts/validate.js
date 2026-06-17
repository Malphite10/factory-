const fs = require('fs');
const path = require('path');
const Ajv = require('ajv');
const addFormats = require('ajv-formats');

const ajv = new Ajv({ allErrors: true });
addFormats(ajv);

const args = process.argv.slice(2);
const typeIndex = args.indexOf('--type');
const type = typeIndex !== -1 ? args[typeIndex + 1] : null;

if (type === 'schemas') {
  const schemaDir = path.join(__dirname, '../agents/schemas');
  const files = fs.readdirSync(schemaDir);
  let success = true;

  files.forEach(file => {
    try {
      const schema = JSON.parse(fs.readFileSync(path.join(schemaDir, file), 'utf8'));
      ajv.compile(schema);
      console.log(`✓ Schema valid: ${file}`);
    } catch (e) {
      console.error(`✗ Schema invalid: ${file}`, e.message);
      success = false;
    }
  });

  process.exit(success ? 0 : 1);
} else {
  console.log('Validation type not implemented yet.');
  process.exit(0);
}
