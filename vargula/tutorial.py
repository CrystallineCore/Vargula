"""
Vargula Grand Demo - A Complete Feature Showcase
================================================
This demo showcases all major features of the Vargula terminal styling library
including color palettes, tables, progress bars, accessibility, and more.
"""

import vargula
import time
import random

vg = vargula.Vargula()

def section_header(title):
    """Print a fancy section header"""
    width = 80
    vg.write(f"\n{'='*width}")
    vg.write(f"<bold><cyan>{title.center(width)}</cyan></bold>")
    vg.write(f"{'='*width}\n")


def demo_basic_styling():
    """Demonstrate basic text styling"""
    section_header("BASIC TEXT STYLING")
    
    # Colors
    vg.write("<bold>Colors:</bold>")
    vg.write("<red>Red</red> | <green>Green</green> | <blue>Blue</blue> | "
             "<yellow>Yellow</yellow> | <magenta>Magenta</magenta> | <cyan>Cyan</cyan>")
    
    # Looks
    vg.write("\n<bold>Text Styles:</bold>")
    vg.write("<bold>Bold</bold> | <dim>Dim</dim> | <italic>Italic</italic> | "
             "<underline>Underline</underline> | <strikethrough>Strikethrough</strikethrough>")
    
    # Combinations
    vg.write("\n<bold>Combinations:</bold>")
    vg.write("<bold><red>Bold Red</red></bold> | "
             "<underline><blue>Underlined Blue</blue></underline> | "
             "<italic><green>Italic Green</green></italic>")
    
    # Hex colors
    vg.write("\n<bold>Hex Colors:</bold>")
    vg.write("<#FF1493>Deep Pink</#FF1493> | "
             "<#7FFF00>Chartreuse</#7FFF00> | "
             "<#FF6347>Tomato</#FF6347> | "
             "<#4169E1>Royal Blue</#4169E1>")
    
    # Backgrounds
    vg.write("\n<bold>Backgrounds:</bold>")
    vg.write("<white><@red>Red BG</@red></white> | "
             "<black><@yellow>Yellow BG</@yellow></black> | "
             "<white><@blue>Blue BG</@blue></white> | "
             "<black><@#FF69B4>Pink BG</@#FF69B4></black>")


def demo_custom_styles():
    """Demonstrate custom style creation"""
    section_header("CUSTOM STYLES & THEMES")
    
    # Create custom styles
    vg.create("success", color="bright_green", look="bold")
    vg.create("error", color="bright_red", look="bold")
    vg.create("warning", color="bright_yellow", look="bold")
    vg.create("info", color="bright_cyan")
    vg.create("highlight", color="#FFD700", bg="#1a1a1a", look="bold")
    
    vg.write("<bold>Custom Status Styles:</bold>")
    vg.write("<success>✓ Operation successful!</success>")
    vg.write("<error>✗ Fatal error occurred!</error>")
    vg.write("<warning>⚠ Warning: Check your input</warning>")
    vg.write("<info>ℹ Information: Process started</info>")
    vg.write("<highlight>★ Featured content</highlight>")
    
    # Themed output
    vg.write("\n<bold>Setting Dark Theme:</bold>")
    vg.set_theme("dark")
    vg.write("<error>[ERROR]</error> Database connection failed")
    vg.write("<success>[SUCCESS]</success> File uploaded successfully")
    vg.write("<warning>[WARNING]</warning> Disk space low")
    vg.write("<critical>[CRITICAL]</critical> System overheating!")


def demo_palette_generation():
    """Demonstrate palette generation"""
    section_header("COLOR PALETTE GENERATION")
    
    schemes = ["complementary", "analogous", "triadic", "tetradic", "split_complementary"]
    base_colors = ["#e74c3c", "#3498db", "#2ecc71", "#9b59b6", "#f39c12"]
    
    for scheme, base in zip(schemes, base_colors):
        palette = vg.generate_palette(base, scheme, count=6, randomize=True)
        vg.write(f"\n<bold><underline>{scheme.replace('_', ' ').title()} (base: {base})</underline></bold>")
        
        # Show color swatches
        blocks = ""
        for color in palette:
            blocks += vg.style("███", color=color)
        vg.write(blocks)
        
        # Show hex values
        vg.write("  " + " ".join(palette))


def demo_theme_palettes():
    """Demonstrate complete theme generation"""
    section_header("THEME PALETTE GENERATION")
    
    # Generate and apply a theme
    theme = vg.generate_theme_palette("analogous", "#8e44ad", force_semantic_colors=True)
    vg.apply_palette_theme(theme, register_styles=True)
    
    vg.write("<bold>Generated Theme Colors:</bold>\n")
    for name, color in theme.items():
        block = vg.style("████", color=color)
        vg.write(f"  {block} <bold>{name:12s}</bold>: {color}")
    
    vg.write("\n<bold>Theme in Action:</bold>")
    vg.write("<primary>Primary action button</primary>")
    vg.write("<secondary>Secondary button</secondary>")
    vg.write("<accent>Accent highlight</accent>")
    vg.write("<success>✓ Success message</success>")
    vg.write("<warning>⚠ Warning message</warning>")
    vg.write("<error>✗ Error message</error>")


def demo_color_manipulation():
    """Demonstrate color manipulation functions"""
    section_header("COLOR MANIPULATION")
    
    base = "#3498db"
    vg.write(f"<bold>Base Color:</bold> {vg.style('█████', color=base)} {base}\n")
    
    # Lighten/Darken
    vg.write("<bold>Lightness Variations:</bold>")
    colors_light = [vg.darken(base, 0.3), vg.darken(base, 0.15), base, 
                    vg.lighten(base, 0.15), vg.lighten(base, 0.3)]
    for i, c in enumerate(colors_light):
        vg.write(f"  {vg.style('███', color=c)} {c}")
    
    # Saturation
    vg.write("\n<bold>Saturation Variations:</bold>")
    colors_sat = [vg.desaturate(base, 0.5), vg.desaturate(base, 0.25), base,
                  vg.saturate(base, 0.25), vg.saturate(base, 0.5)]
    for c in colors_sat:
        vg.write(f"  {vg.style('███', color=c)} {c}")
    
    # Hue shifts
    vg.write("\n<bold>Hue Rotation (60° increments):</bold>")
    hues = [vg.shift_hue(base, deg) for deg in range(0, 360, 60)]
    blocks = "".join([vg.style("████", color=c) for c in hues])
    vg.write(f"  {blocks}")
    
    # Mixing
    vg.write("\n<bold>Color Mixing (#e74c3c + #3498db):</bold>")
    mix_blocks = ""
    for w in [0, 0.25, 0.5, 0.75, 1.0]:
        mixed = vg.mix("#e74c3c", "#3498db", w)
        mix_blocks += vg.style("████", color=mixed)
    vg.write(f"  {mix_blocks}")


def demo_accessibility():
    """Demonstrate accessibility features"""
    section_header("ACCESSIBILITY FEATURES")
    
    # Contrast ratios
    vg.write("<bold>WCAG Contrast Ratio Testing:</bold>\n")
    pairs = [
        ("#FFFFFF", "#000000", "Black on White"),
        ("#3498db", "#FFFFFF", "Blue on White"),
        ("#e74c3c", "#1a1a1a", "Red on Dark Gray"),
        ("#95a5a6", "#2c3e50", "Gray on Navy"),
    ]
    
    for fg, bg, desc in pairs:
        ratio = vg.calculate_contrast_ratio(fg, bg)
        aa = vg.meets_wcag(fg, bg, "AA")
        aaa = vg.meets_wcag(fg, bg, "AAA")
        
        sample = vg.style(f" {desc} ", color=fg, bg=bg)
        status_aa = vg.style("AA ✓", color="green") if aa else vg.style("AA ✗", color="red")
        status_aaa = vg.style("AAA ✓", color="green") if aaa else vg.style("AAA ✗", color="red")
        
        vg.write(f"  {sample} Ratio: {ratio:.2f} | {status_aa} | {status_aaa}")
    
    # Color blindness simulation
    vg.write("\n<bold>Color Blindness Simulation:</bold>\n")
    test_colors = ["#e74c3c", "#2ecc71", "#3498db", "#f39c12"]
    cb_types = ["protanopia", "deuteranopia", "tritanopia"]
    
    vg.write("  Original:    " + "".join([vg.style("████", color=c) for c in test_colors]))
    for cb_type in cb_types:
        simulated = [vg.simulate_colorblindness(c, cb_type) for c in test_colors]
        blocks = "".join([vg.style("████", color=c) for c in simulated])
        vg.write(f"  {cb_type:13s} {blocks}")


def demo_tables():
    """Demonstrate table creation"""
    section_header("RICH TABLES")
    
    # Basic table
    vg.write("<bold>Employee Directory:</bold>\n")
    table1 = vg.Table(
        title="🏢 Tech Company Staff",
        style="cyan",
        header_style="bold yellow",
        border_style="bright_blue",
        box="rounded",
        show_lines=False
    )
    
    table1.add_column("ID", style="dim", justify="right", width=6)
    table1.add_column("Name", style="bold cyan", min_width=15)
    table1.add_column("Department", style="magenta", min_width=15)
    table1.add_column("Status", justify="center", width=10)
    table1.add_column("Salary", style="green", justify="right", width=12)
    
    employees = [
        ("E001", "Alice Johnson", "Engineering", "✓ Active", "$120,000"),
        ("E002", "Bob Smith", "Marketing", "✓ Active", "$95,000"),
        ("E003", "Carol Davis", "Design", "⚠ Leave", "$105,000"),
        ("E004", "David Chen", "Engineering", "✓ Active", "$115,000"),
        ("E005", "Emma Wilson", "Sales", "✗ Inactive", "$88,000"),
    ]
    
    for emp in employees:
        table1.add_row(*emp)
    
    print(table1)
    
    # Stats table
    vg.write("\n<bold>System Statistics:</bold>\n")
    table2 = vg.Table(
        caption="Last updated: 2024",
        border_style="green",
        box="double",
        show_lines=True
    )
    
    table2.add_column("Metric", style="bold", min_width=20)
    table2.add_column("Value", style="cyan", justify="right", width=15)
    table2.add_column("Status", justify="center", width=12)
    
    table2.add_row("CPU Usage", "67%", vg.style("Normal", color="green"))
    table2.add_row("Memory", "4.2 GB / 16 GB", vg.style("Good", color="green"))
    table2.add_row("Disk Space", "89%", vg.style("Warning", color="yellow"))
    table2.add_row("Network", "125 Mbps", vg.style("Excellent", color="green"))
    table2.add_row("Uptime", "23 days 4 hours", vg.style("Stable", color="cyan"))
    
    print(table2)


def demo_progress_bars():
    """Demonstrate progress bars"""
    section_header("PROGRESS BARS")
    
    vg.write("<bold>Single Progress Bar:</bold>\n")
    
    # Simulated file download
    with vg.ProgressBar(
        total=100,
        desc="Downloading",
        complete_style="green",
        incomplete_style="bright_black",
        percentage_style="cyan",
        desc_style="bold yellow",
        bar_width=40
    ) as pbar:
        for i in range(100):
            time.sleep(0.02)
            pbar.update(1)
    
    vg.write("\n<bold>Multiple Progress Bars:</bold>\n")
    
    # Multi-progress example
    tasks_data = [
        ("Compiling modules", 80),
        ("Running tests", 120),
        ("Building package", 60),
    ]
    
    with vg.MultiProgress() as mp:
        tasks = []
        for desc, total in tasks_data:
            task_id = mp.add_task(
                desc,
                total=total,
                complete_style="cyan",
                percentage_style="yellow"
            )
            tasks.append((task_id, total))
        
        # Simulate work
        for _ in range(max(t[1] for t in tasks)):
            for task_id, total in tasks:
                if random.random() > 0.3:  # Random progress
                    mp.update(task_id, 1)
            time.sleep(0.02)


def demo_advanced_formatting():
    """Demonstrate advanced formatting features"""
    section_header("ADVANCED FORMATTING")
    
    # Nested tags
    vg.write("<bold>Nested Styling:</bold>")
    vg.write("<cyan>This is cyan with <bold>bold text</bold> and <underline>underlined</underline> parts</cyan>")
    vg.write("<#FF6347>Hex color with <bold><underline>multiple effects</underline></bold> combined</#FF6347>")
    
    # Escape sequences
    vg.write("\n<bold>Escape Sequences:</bold>")
    vg.write(r"Use \< and \> to show literal angle brackets: \<not a tag\>")
    vg.write("This <red>is red</red> but this \\<red>is not\\</red>")
    
    # Complex combinations
    vg.write("\n<bold>Complex Combinations:</bold>")
    vg.write("<bold><white><@#2c3e50>Header Text</@#2c3e50></white></bold>")
    vg.write("<italic><#9b59b6>Purple italic <bold>with bold section</bold> inside</#9b59b6></italic>")
    
    # Using write function
    vg.write("\n<bold>Write Function (like print):</bold>")
    vg.write("<green>Success:</green>", "Operation completed in", "<yellow>2.5s</yellow>", sep=" | ")
    vg.write("<red>Error:</red>", "Connection timeout", end=" [Code: 408]\n")


def demo_practical_examples():
    """Show practical usage examples"""
    section_header("PRACTICAL EXAMPLES")
    
    # Log output
    vg.write("<bold>Application Log Output:</bold>\n")
    log_entries = [
        ("INFO", "cyan", "Application started successfully"),
        ("DEBUG", "bright_black", "Loading configuration from config.yml"),
        ("INFO", "cyan", "Connected to database: postgresql://localhost"),
        ("WARNING", "yellow", "Cache miss for key 'user:1234'"),
        ("ERROR", "red", "Failed to send email to user@example.com"),
        ("INFO", "cyan", "Request processed in 145ms"),
    ]
    
    for level, color, message in log_entries:
        timestamp = vg.style("2024-01-15 10:30:45", color="dim")
        level_text = vg.style(f"[{level:8s}]", color=color, look="bold")
        vg.write(f"{timestamp} {level_text} {message}")
    
    # CLI Output
    vg.write("\n<bold>CLI Tool Output:</bold>\n")
    vg.write("<bold><green>✓</green></bold> Initialized git repository")
    vg.write("<bold><yellow>↓</yellow></bold> Installing dependencies...")
    vg.write("  <dim>├──</dim> react@18.2.0")
    vg.write("  <dim>├──</dim> typescript@5.0.0")
    vg.write("  <dim>└──</dim> vite@4.3.0")
    vg.write("<bold><green>✓</green></bold> Installation complete!")
    vg.write("<bold><cyan>→</cyan></bold> Run <cyan>npm start</cyan> to begin")


def demo_color_theory():
    """Demonstrate color theory visualization"""
    section_header("COLOR THEORY VISUALIZATION")
    
    base = "#e74c3c"
    vg.write(f"<bold>Base Color:</bold> {vg.style('█████', color=base)} {base}\n")
    
    # Show different harmonies
    harmonies = [
        ("Monochromatic", "monochromatic"),
        ("Analogous", "analogous"),
        ("Complementary", "complementary"),
        ("Split Complementary", "split_complementary"),
        ("Triadic", "triadic"),
        ("Tetradic", "tetradic"),
    ]
    
    for name, scheme in harmonies:
        palette = vg.generate_palette(base, scheme, count=5)
        blocks = "".join([vg.style("████", color=c) for c in palette])
        vg.write(f"<bold>{name:20s}</bold> {blocks}")


def main():
    """Run the grand demo"""
    # ASCII Art Title
    title = r"""
    ╦  ╦╔═╗╦═╗╔═╗╦ ╦╦  ╔═╗  ╔═╗╦═╗╔═╗╔╗╔╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗
    ╚╗╔╝╠═╣╠╦╝║ ╦║ ║║  ╠═╣  ║ ╦╠╦╝╠═╣║║║ ║║   ║║║╣ ║║║║ ║
     ╚╝ ╩ ╩╩╚═╚═╝╚═╝╩═╝╩ ╩  ╚═╝╩╚═╩ ╩╝╚╝═╩╝  ═╩╝╚═╝╩ ╩╚═╝
    """
    
    vg.write(f"<bold><cyan>{title}</cyan></bold>")
    vg.write("<bold><yellow>Complete Feature Showcase & Tutorial</yellow></bold>")
    vg.write("<dim>Press Ctrl+C to exit at any time</dim>\n")
    
    try:
        # Run all demos
        demo_basic_styling()
        time.sleep(0.5)
        
        demo_custom_styles()
        time.sleep(0.5)
        
        demo_palette_generation()
        time.sleep(0.5)
        
        demo_theme_palettes()
        time.sleep(0.5)
        
        demo_color_manipulation()
        time.sleep(0.5)
        
        demo_accessibility()
        time.sleep(0.5)
        
        demo_tables()
        time.sleep(0.5)
        
        demo_progress_bars()
        time.sleep(0.5)
        
        demo_advanced_formatting()
        time.sleep(0.5)
        
        demo_practical_examples()
        time.sleep(0.5)
        
        demo_color_theory()
        
        # Finale
        section_header("DEMO COMPLETE")
        vg.write("<bold><green>✓ All features demonstrated successfully!</green></bold>")
        vg.write("<cyan>Visit the documentation for more details and examples.</cyan>")
        vg.write(f"\n<dim>Vargula v{vg.__version__} - Simple, powerful terminal styling</dim>\n")
        
    except KeyboardInterrupt:
        vg.write("\n\n<yellow>Demo interrupted by user.</yellow>")
    except Exception as e:
        vg.write(f"\n\n<bold><red>Error:</red></bold> {e}")


if __name__ == "__main__":
    main()