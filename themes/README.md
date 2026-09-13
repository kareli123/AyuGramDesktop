# Apple Liquid Glass themes

iOS/macOS-inspired palettes for AyuGram / Telegram Desktop.

| File | Look |
| --- | --- |
| `apple-liquid-glass-dark.tdesktop-palette` | Graphite panels, iOS blue accent, iMessage-blue outgoing bubbles |
| `apple-liquid-glass-light.tdesktop-palette` | iOS gray background, white cards, gray/blue iMessage bubbles |
| `apple-liquid-glass-dark-translucent.tdesktop-palette` | Same as dark, but panels carry alpha — needs `AYUGRAM_GLASS` (see below) |

## Install (no build required)

These work in any current AyuGram / Telegram Desktop build:

1. **Settings → Chat Settings → Themes → ⋮ → Create from file**, pick the
   `.tdesktop-palette` file. *(or)*
2. Simply **drag the `.tdesktop-palette` file onto the app window**.

Keys not listed in a palette fall back to the built-in day/night theme, so
these files stay small and only override what gives the Apple look.

## Real glass (Windows)

A palette alone cannot make panels see-through — the window has to be
translucent and the compositor has to draw a blurred material behind it. That
part lives in `Telegram/SourceFiles/platform/win/main_window_win.cpp` and is
opt-in via an environment variable, so the default build is untouched:

```bat
set AYUGRAM_GLASS=acrylic
AyuGram.exe
```

| Value | Effect |
| --- | --- |
| `mica` | Windows 11 22H2+ Mica — subtle, tinted by the desktop wallpaper |
| `acrylic` | Stronger, more translucent acrylic (closest to Apple's look) |
| `tabbed` | Mica Alt |
| `blur` | Forces the legacy Windows 10 blur-behind path |
| unset | Default opaque window |

Implementation notes:

- Windows 11 22H2+ uses the documented `DWMWA_SYSTEMBACKDROP_TYPE`.
- Windows 11 21H2 falls back to the undocumented `DWMWA_MICA_EFFECT`.
- Windows 10 falls back to the undocumented `ACCENT_POLICY` blur-behind.
- The blur itself is done by the compositor, so there is **no per-frame CPU
  cost** — this is why it is preferred over a custom GL blur pass.

Pair it with `apple-liquid-glass-dark-translucent.tdesktop-palette`, otherwise
the panels stay opaque and you will not see any difference.

> **Status:** the Win32 side is implemented, but the combination of Qt's
> `WA_TranslucentBackground` and a DWM backdrop still needs verifying on a real
> build — Qt may back translucent windows with a layered window, which can
> suppress the material. Expect to iterate here.

## Notes

- Blur of *in-app* content underneath panels (e.g. the chat behind the top
  bar) is a different, heavier problem and would need a shader in the client's
  own renderer. Not covered here.
- Accent colors: system blue `#0A84FF` (dark) / `#007AFF` (light);
  destructive red `#FF453A` / `#FF3B30`.
