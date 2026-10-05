# Theme Name

## Features

## Installation

## Configuration

## Vendored Mermaid bundle

`assets/js/mermaid.min.js` comes from the exact `mermaid` version in
`package.json` and `package-lock.json`. Use Node.js 22.12 or newer.
After changing the version, update `mermaidVendoredAt` in `package.json`,
run `npm install` and `npm run build:vendor`, then commit the lockfile
and generated bundle together. `npm ci && npm run build:vendor` must
leave a clean diff for the bundle.
