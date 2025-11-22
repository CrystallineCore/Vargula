
# Environment Variables

- **`NO_COLOR`**: Disable all styling (respects standard)
- **`FORCE_COLOR`**: Force enable styling even when not TTY

```bash
# Disable colors
NO_COLOR=1 python app.py

# Force colors in pipes
FORCE_COLOR=1 python app.py | less -R
```
