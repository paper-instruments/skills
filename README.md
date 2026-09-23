# Paper Instruments skills

Agent skills for working with Excel, Word, and PowerPoint files through the Paper Instruments Python packages. This repository contains three skills:

| Skill | Files | Python distribution | Import |
| --- | --- | --- | --- |
| `xlsx` | `.xlsx`, `.xlsm` | [`paper-xlsx`](https://github.com/paper-instruments/paper-xlsx) | `openpyxl` |
| `docx` | `.docx` | [`paper-docx`](https://github.com/paper-instruments/paper-docx) | `docx` |
| `pptx` | `.pptx` | [`paper-pptx`](https://github.com/paper-instruments/paper-pptx) | `pptx` |

Each skill includes a Paper API companion and a generated API reference. Those references document `paper-xlsx==0.2.1`, `paper-docx==0.2.0`, and `paper-pptx==0.2.0`, respectively.

## Install all three skills

### Claude Code marketplace

Run these as two separate commands **inside Claude Code**:

```text
/plugin marketplace add paper-instruments/skills
/plugin install paper-office@paper-skills
```

This installs one `paper-office` plugin containing the `xlsx`, `docx`, and `pptx` skills. No Anthropic marketplace submission is required. The source is this GitHub repository.

### Codex marketplace

Run these in a terminal:

```bash
codex plugin marketplace add paper-instruments/skills
codex plugin add paper-office@paper-skills
```

### Direct skill install

The [Skills CLI](https://github.com/vercel-labs/skills) can install the three skills for both agents without using either plugin marketplace:

```bash
npx skills add paper-instruments/skills --skill '*' -a claude-code -a codex -g
```

`-g` installs for the user across projects; omit it to install in the current project. To select only one skill, replace `--skill '*'` with `--skill xlsx`, `--skill docx`, or `--skill pptx`.

## Install the Python packages separately

Installing these skills **does not install the Python distributions**. The skills assume the corresponding Paper distributions are already available in the working Python environment. Follow each package's README for its installation and environment checks before using the skill. The Paper distributions share import names with their upstream packages, so do not install a Paper distribution alongside the upstream distribution that owns the same import tree.

If you use another package release, verify its API and preservation behavior against the bundled reference before relying on the instructions. Updating a Python package does not update an installed skill.

## Source and license

These skills are distributed under the [MIT license](LICENSE). Package source code and Python dependencies are hosted and licensed separately in their own repositories.
