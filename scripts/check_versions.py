"""Check that every version this repository states agrees.

- Each skill's SKILL.md `metadata.version` equals the package version its generated
  API reference was built from (`references/api/index.md`, first line).
- `plugin.json` and `.claude-plugin/plugin.json` carry the same version.

Prints the plugin version on success, so the release workflow can tag it.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GENERATED = re.compile(r"Generated from \S+ (\d+\.\d+\.\d+\S*) docstrings")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
VERSION = re.compile(r'^  version: "?([^"\n]+)"?$', re.MULTILINE)


def main() -> int:
    errors = []
    for skill in sorted((ROOT / "skills").iterdir()):
        text = (skill / "SKILL.md").read_text()
        frontmatter = FRONTMATTER.match(text)
        stated = VERSION.search(frontmatter.group(1)) if frontmatter else None
        generated = GENERATED.search((skill / "references/api/index.md").read_text().splitlines()[0])
        if not stated:
            errors.append(f"{skill.name}: SKILL.md has no metadata.version")
        elif not generated:
            errors.append(f"{skill.name}: references/api/index.md does not say which version it was generated from")
        elif stated.group(1) != generated.group(1):
            errors.append(
                f"{skill.name}: SKILL.md says {stated.group(1)}, the API reference was generated from {generated.group(1)}"
            )
    versions = {path: json.loads((ROOT / path).read_text())["version"] for path in ("plugin.json", ".claude-plugin/plugin.json")}
    if len(set(versions.values())) != 1:
        errors.append(f"plugin versions differ: {versions}")
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(next(iter(versions.values())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
