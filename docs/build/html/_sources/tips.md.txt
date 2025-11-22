#  Tips & Best Practices

## 1. Use Themes for Consistency
```python
vg.set_theme("dark")  # or generate custom theme
vg.write("<error>Error</error> vs <success>Success</success>")
```

## 2. Test Accessibility Early
```python
theme = vg.generate_accessible_theme("#3498db", wcag_level="AA")
```

## 3. Validate for Colorblindness
```python
is_safe, _ = vg.validate_colorblind_safety(my_colors)
```

## 4. Save and Reuse Palettes
```python
vg.save_palette(colors, "brand_colors.json")
# Later...
colors, _ = vg.load_palette("brand_colors.json")
```

## 5. Nest Styles for Complex Formatting
```python
vg.write("<bold>Bold with <red>red</red> and <blue>blue</blue></bold>")
```

