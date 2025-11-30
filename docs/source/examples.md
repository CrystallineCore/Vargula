# Examples

## Example 1: Color Palette Explorer

```python
from vargula import Vargula
vg = Vargula()

# Generate and preview different color schemes
schemes = ["analogous", "complementary", "triadic", "tetradic"]

for scheme in schemes:
    print(vg.format(f"\n<bold><cyan>{scheme.upper()} Palette</cyan></bold>"))
    palette = vg.generate_palette("#3498db", scheme, count=6)
    print(vg.preview_palette(palette, width=30))
    
    # Check accessibility
    is_safe, problems = vg.validate_colorblind_safety(palette)
    if is_safe:
        print(vg.format("<green>✓ Colorblind-safe</green>"))
    else:
        print(vg.format(f"<yellow>⚠ {len(problems)} similar color pairs</yellow>"))
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-09-58.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-09-58.png?raw=true)

## Example 2: Themed CLI Application

```python
from vargula import Vargula
import time

vg = Vargula()

# Generate and apply theme
theme = vg.generate_theme_palette("analogous", "#e74c3c")
vg.apply_palette_theme(theme)

# Create custom log styles
vg.create("timestamp", color="#666666")
vg.create("user", color="cyan", look="bold")

# Styled output
vg.write("<timestamp>[12:34:56]</timestamp> <user>admin</user> logged in")
vg.write("<success>✓ Database connection established</success>")
vg.write("<warning>⚠ Cache expiring soon</warning>")
vg.write("<error>✗ Failed to connect to API</error>")

# Progress with theme colors
with vg.ProgressBar(
    total=100,
    desc="Syncing",
    complete_style="primary",
    percentage_style="accent"
) as pbar:
    for i in range(100):
        pbar.update(1)
        time.sleep(0.02)
```

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/update.gif?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/update.gif?raw=true)


## Example 3: Accessible Theme Generator

```python
from vargula import Vargula
vg = Vargula()

# Generate accessible theme for light background
theme = vg.generate_accessible_theme(
    base_color="#3498db",
    scheme="complementary",
    background="#ffffff",
    wcag_level="AAA"
)

# Verify contrast ratios
vg.write("<bold>Theme Accessibility Report</bold>\n")

for name, color in theme.items():
    if name in ["primary", "secondary", "error", "success"]:
        ratio = vg.calculate_contrast_ratio(color, theme["background"])
        meets_aa = vg.meets_wcag(color, theme["background"], "AA")
        meets_aaa = vg.meets_wcag(color, theme["background"], "AAA")
        
        status = "AAA ✓" if meets_aaa else ("AA ✓" if meets_aa else "✗")
        print(f"{name:12s} {color}  Ratio: {ratio:.2f}  {status}")
```

**Output:**
```text
Theme Accessibility Report

primary      #2a7cb4  Ratio: 4.53  AA ✓
secondary    #a75a27  Ratio: 5.08  AA ✓
success      #277f26  Ratio: 5.06  AA ✓
error        #d82b2b  Ratio: 4.88  AA ✓
```

## Example 4: Data Table with Styling

```python
from vargula import Vargula
vg = Vargula()

# Create styled table
table = vg.Table(
    title="Q4 2024 Sales Report",
    caption="All figures in USD",
    title_style="bold cyan",
    border_style="blue",
    box="double",
    show_lines=True
)

table.add_column("Region", style="bold", justify="left", width=15)
table.add_column("Revenue", style="green", justify="right", width=12)
table.add_column("Growth", style="cyan", justify="center", width=10)
table.add_column("Status", justify="center", width=10)

# Add data with conditional styling
table.add_row("North America", "$1,250,000", "+15.3%", "🟢")
table.add_row("Europe", "$890,000", "+8.7%", "🟢")
table.add_row("Asia Pacific", "$1,500,000", "+22.1%", "🟢")
table.add_row("Latin America", "$450,000", "-2.4%", "🔴", style="dim")

print(table)
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-14-56.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-14-56.png?raw=true)


## Example 5: Multi-Progress Task Manager

```python
from vargula import Vargula
import time
import random

vg = Vargula()

tasks = [
    ("Downloading files", 150),
    ("Processing data", 100),
    ("Uploading results", 80),
    ("Cleaning up", 50)
]

with vg.MultiProgress() as mp:
    # Create all tasks
    task_ids = [
        mp.add_task(desc, total=total, complete_style="green")
        for desc, total in tasks
    ]
    
    # Simulate concurrent progress
    while any(mp.tasks[tid]["progress"].current < mp.tasks[tid]["progress"].total 
              for tid in task_ids):
        for tid in task_ids:
            if mp.tasks[tid]["progress"].current < mp.tasks[tid]["progress"].total:
                mp.update(tid, random.randint(1, 5))
        time.sleep(0.05)
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-16-06.gif?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screencast%20from%202025-11-22%2008-16-06.gif?raw=true)


## Example 6: Color Manipulation

```python
from vargula import Vargula
vg = Vargula()

base = "#3498db"

print(vg.format(f"<bold>Base Color:</bold> {base}"))
print(vg.style("█" * 40, color=base))

# Lightness variations
print(vg.format("\n<bold>Lightness:</bold>"))
for i in range(5):
    amount = (i - 2) * 0.2
    color = vg.lighten(base, amount) if amount > 0 else vg.darken(base, -amount)
    print(f"{amount:+.1f}  {color}  " + vg.style("█" * 30, color=color))

# Saturation variations
print(vg.format("\n<bold>Saturation:</bold>"))
for i in range(5):
    amount = i * 0.2
    color = vg.desaturate(base, amount)
    print(f"-{amount:.1f}  {color}  " + vg.style("█" * 30, color=color))

# Hue rotation
print(vg.format("\n<bold>Hue Rotation:</bold>"))
for degrees in [0, 60, 120, 180, 240, 300]:
    color = vg.shift_hue(base, degrees)
    print(f"{degrees:3d}°  {color}  " + vg.style("█" * 30, color=color))

# Color mixing
print(vg.format("\n<bold>Mixing with Red:</bold>"))
for weight in [0, 0.25, 0.5, 0.75, 1.0]:
    color = vg.mix("#FF0000", base, weight)
    print(f"{weight:.2f}  {color}  " + vg.style("█" * 30, color=color))
```
[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-18-34.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-18-34.png?raw=true)

## Example 7: Colorblind Simulation

```python
from vargula import Vargula
vg = Vargula()

colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF"]
cb_types = ["protanopia", "deuteranopia", "tritanopia"]

print(vg.format("<bold>Original Palette:</bold>"))
print(vg.preview_palette(colors, width=20, show_info=False))

for cb_type in cb_types:
    print(vg.format(f"\n<bold>{cb_type.title()} Simulation:</bold>"))
    simulated = [vg.simulate_colorblindness(c, cb_type) for c in colors]
    print(vg.preview_palette(simulated, width=20, show_info=False))
    
    is_safe, problems = vg.validate_colorblind_safety(colors, cb_type)
    if not is_safe:
        print(vg.format(f"<yellow>⚠ {len(problems)} problematic pairs</yellow>"))
```

[![Demo](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-18-59.png?raw=true)](https://github.com/CrystallineCore/assets/blob/main/vargula/Screenshot%20from%202025-11-22%2008-18-59.png?raw=true)

