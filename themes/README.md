# Apple Liquid Glass themes

iOS/macOS-inspired palettes for AyuGram / Telegram Desktop.

| File | Look |
| --- | --- |
| `apple-liquid-glass-dark.tdesktop-palette` | Graphite panels, iOS blue accent, iMessage-blue outgoing bubbles |
| `apple-liquid-glass-light.tdesktop-palette` | iOS gray background, white cards, gray/blue iMessage bubbles |

## Install (no build required)

These work in any current AyuGram / Telegram Desktop build:

1. **Settings → Chat Settings → Themes → ⋮ → Create from file**, pick the
   `.tdesktop-palette` file. *(or)*
2. Simply **drag the `.tdesktop-palette` file onto the app window**.

Keys not listed in a palette fall back to the built-in day/night theme, so
these files stay small and only override what gives the Apple look.

## Notes

- True translucency / "liquid glass" blur (mica/acrylic + backdrop blur under
  panels) is a separate rendering change — a palette alone cannot make panels
  see-through. See the `apple-liquid-glass` branch for the code work.
- Accent colors: system blue `#0A84FF` (dark) / `#007AFF` (light);
  destructive red `#FF453A` / `#FF3B30`.
