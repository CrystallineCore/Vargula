#  WCAG Contrast Guidelines

| Level | Normal Text | Large Text |
|-------|-------------|-------------|
| **AA** | 4.5:1 | 3:1 |
| **AAA** | 7:1 | 4.5:1 |

*Large text* = 18pt+ or 14pt+ bold

```python
# Check if colors meet WCAG AA
if vg.meets_wcag(text_color, bg_color, "AA"):
    print("Accessible!")

# Automatically fix contrast
accessible_color = vg.ensure_contrast(text_color, bg_color, min_ratio=4.5)
```
