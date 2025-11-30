# Frequently Asked Questions

<meta name="description" content="Common questions about Vargula Python terminal styling library - installation, usage, accessibility, and troubleshooting.">
<meta name="keywords" content="vargula faq, python terminal styling questions, colorblind accessible terminal, wcag terminal colors">

---

## Installation & Setup

### **Q: How do I install Vargula?**

A: Install via pip:

```bash
pip install vargula
```

### **Q: What Python versions are supported?**

A: Vargula supports Python **3.7 and above**.

### **Q: Does Vargula work on Windows?**

A: Yes! Vargula works on **Windows, macOS, and Linux**.

---

## Color & Styling

### **Q: How do I create accessible color palettes?**

A: Use the `generate_accessible_theme()` function:

```python
from vargula import Vargula

vg = Vargula()

theme = vg.generate_accessible_theme(
    "#3498db",
    wcag_level="AA",
    background="#ffffff"
)
```

### **Q: Can I validate colors for colorblind users?**

A: Yes! Use `validate_colorblind_safety()`:

```python
is_safe, problems = vg.validate_colorblind_safety(
    colors,
    cb_type="deuteranopia"
)
```

### **Q: What color schemes are available?**

A: Vargula supports **7 color harmony schemes**:

* Monochromatic
* Analogous
* Complementary
* Split Complementary
* Triadic
* Tetradic
* Square

---

## Comparison with Other Libraries

### **Q: How is Vargula different from Rich?**

A:
Rich focuses on comprehensive terminal UI features (layouts, syntax highlighting, markdown).
Vargula specializes in **color design and accessibility**, offering features like:

* color palette generation
* WCAG validation
* colorblind simulation

### **Q: Should I use Vargula or Colorama?**

A:
Use **Colorama** if you only need basic cross-platform ANSI support.
Use **Vargula** if you need:

* color theory
* accessibility tools
* markup syntax
* rich components (tables, progress bars)

See the detailed **[comparison](comparison.md)** page for more information.

---

## Troubleshooting

### **Q: Colors aren't showing in my terminal**

A: Check if your terminal supports ANSI colors. Most do.

Test it:

```python
from vargula import Vargula
vg = Vargula()
vg.write("<red>Test</red>")
```

### **Q: How do I disable colors temporarily?**

Use `vg.disable()` and `vg.enable()`:

```python
vg.disable()  # Disable styling
print(vg.style("No color", color="red"))
vg.enable()   # Re-enable styling
```

### **Q: My custom theme isn't working**

A: Ensure you applied it using `apply_palette_theme()`:

```python
theme = vg.generate_theme_palette("triadic")
vg.apply_palette_theme(theme)
vg.write("<primary>Now it works!</primary>")
```

---

## More Questions?

Can't find your answer? Check:

* **[API Documentation](api.md)** – complete API reference
* **[GitHub Issues](https://github.com/crystallinecore/vargula/issues)** – report bugs or ask questions
* **[Examples](examples.md)** – more code examples

