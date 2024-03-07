// ESM

const { Notebook } = require('crossnote');

async function main() {
  const notebook = await
   Notebook.init({
    notebookPath: __dirname,
    config: {
      previewTheme: 'github-light.css',
      mathRenderingOption: 'KaTeX',
      codeBlockTheme: 'github.css',
      printBackground: true,
      enableScriptExecution: true, // <= For running code chunks.
      enableExtendedTableSyntax: true,
    },
  });
  const engine = notebook.getNoteMarkdownEngine(process.argv[2]);
  await engine.htmlExport({ offline: false, runAllCodeChunks: true });
  return process.exit();
}

main();