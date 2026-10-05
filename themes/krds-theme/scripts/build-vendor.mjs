import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const theme = fileURLToPath(new URL('../', import.meta.url));
const packageConfig = JSON.parse(await readFile(new URL('../package.json', import.meta.url), 'utf8'));
const version = packageConfig.dependencies.mermaid;
const installedPackage = JSON.parse(await readFile(new URL('../node_modules/mermaid/package.json', import.meta.url), 'utf8'));

if (installedPackage.version !== version || !/^\d{4}-\d{2}-\d{2}$/.test(packageConfig.mermaidVendoredAt)) {
  throw new Error('The installed Mermaid version or vendoring date does not match package.json');
}

const bundle = await readFile(new URL('../node_modules/mermaid/dist/mermaid.min.js', import.meta.url));
const header = `/*! mermaid v${version}, fetched ${packageConfig.mermaidVendoredAt} from official npm dist/mermaid.min.js (unmodified) */\n`;
await writeFile(new URL('../assets/js/mermaid.min.js', import.meta.url), Buffer.concat([Buffer.from(header), bundle]));
console.log(`Wrote ${theme}assets/js/mermaid.min.js from mermaid@${version}`);
