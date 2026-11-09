document.addEventListener("DOMContentLoaded", async () => {
  const nodes = [...document.querySelectorAll("pre.mermaid")];

  if (nodes.length > 0) {
    await mermaid.run({ nodes });
  }
});
