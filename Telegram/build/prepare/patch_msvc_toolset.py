"""Teach libvpx's configure about the v145 platform toolset.

Upstream ships `x86_64-win64-vs17`, which makes gen_msvs_vcxproj.sh emit no
PlatformToolset at all, so MSBuild falls back to v143 (VS 2022 build tools).
That fails with MSB8020 on installations that only have the v145 toolset from
Visual Studio 2026.

libvpx already derives the toolset from the 4th dash-separated field of the
target, and the bundled 0005-add-arm64-v145-toolset.patch already whitelists
`v1[0-9][0-9]` in gen_msvs_vcxproj.sh — only the x86_64 target name is
missing from configure's platform list. Add it.

Run from the libvpx checkout; idempotent.
"""

import sys

ANCHOR = 'all_platforms="${all_platforms} x86_64-win64-vs17"'
ADDED = 'all_platforms="${all_platforms} x86_64-win64-vs17-v145"'


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'configure'
    with open(path, 'r', encoding='utf-8', newline='') as f:
        text = f.read()

    if ADDED in text:
        print('patch_msvc_toolset: already present, nothing to do.')
        return 0
    if ANCHOR not in text:
        print('patch_msvc_toolset: anchor not found in ' + path, file=sys.stderr)
        return 1

    # Keep the file's existing line endings by reusing the anchor line.
    text = text.replace(ANCHOR, ANCHOR + '\n' + ADDED, 1)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    print('patch_msvc_toolset: added ' + ADDED)
    return 0


if __name__ == '__main__':
    sys.exit(main())
