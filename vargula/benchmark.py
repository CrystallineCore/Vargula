"""
Comprehensive benchmark comparing vargula, Rich, and colorama
Tests import time, basic styling, complex operations, and real-world usage
"""
import time
import sys
from io import StringIO

def measure_time(func, iterations=1):
    """Measure execution time of a function"""
    start = time.perf_counter()
    for _ in range(iterations):
        func()
    return (time.perf_counter() - start) * 1000 / iterations


def benchmark_imports():
    """Measure import time for each library"""
    print("=" * 70)
    print("1. IMPORT TIME BENCHMARK")
    print("=" * 70)
    
    # Fresh imports by removing from sys.modules
    modules_to_remove = [m for m in sys.modules if m.startswith(('vargula', 'rich', 'colorama'))]
    for mod in modules_to_remove:
        del sys.modules[mod]
    
    # vargula
    start = time.perf_counter()
    import vargula
    vg_time = (time.perf_counter() - start) * 1000
    
    # Remove and re-measure Rich
    modules_to_remove = [m for m in sys.modules if m.startswith('rich')]
    for mod in modules_to_remove:
        del sys.modules[mod]
    
    start = time.perf_counter()
    from rich.console import Console
    from rich.table import Table as RichTable
    from rich.progress import Progress
    rich_time = (time.perf_counter() - start) * 1000
    
    # Remove and re-measure colorama
    modules_to_remove = [m for m in sys.modules if m.startswith('colorama')]
    for mod in modules_to_remove:
        del sys.modules[mod]
    
    start = time.perf_counter()
    import colorama
    colorama_time = (time.perf_counter() - start) * 1000
    
    print(f"vargula:  {vg_time:6.2f}ms")
    print(f"Rich:     {rich_time:6.2f}ms  ({rich_time/vg_time:5.1f}x)")
    print(f"colorama: {colorama_time:6.2f}ms  ({colorama_time/vg_time:5.1f}x)")
    print()


def benchmark_basic_styling():
    """Benchmark basic text styling operations"""
    print("=" * 70)
    print("2. BASIC STYLING BENCHMARK (10,000 iterations)")
    print("=" * 70)
    
    import vargula 
    vg = vargula.Vargula()
    from rich.console import Console
    import colorama
    from colorama import Fore, Style
    
    colorama.init()
    console = Console(file=StringIO())  # Don't print to stdout
    iterations = 10000
    
    # vargula - style() function
    vg_time = measure_time(
        lambda: vg.style("Hello World", color="red", look="bold"),
        iterations
    )
    
    # Rich - markup
    rich_time = measure_time(
        lambda: console.render_str("[red bold]Hello World[/]"),
        iterations
    )
    
    # colorama - manual codes
    colorama_time = measure_time(
        lambda: f"{Fore.RED}{Style.BRIGHT}Hello World{Style.RESET_ALL}",
        iterations
    )
    
    print(f"vargula:  {vg_time:6.3f}ms")
    print(f"Rich:     {rich_time:6.3f}ms  ({rich_time/vg_time:5.1f}x)")
    print(f"colorama: {colorama_time:6.3f}ms  ({colorama_time/vg_time:5.1f}x)")
    print()


def benchmark_markup_parsing():
    """Benchmark markup/tag parsing performance"""
    print("=" * 70)
    print("3. MARKUP PARSING BENCHMARK (5,000 iterations)")
    print("=" * 70)
    
    import vargula 
    vg = vargula.Vargula()
    from rich.console import Console
    
    console = Console(file=StringIO())
    iterations = 5000
    
    markup_text = "<red>Error:</red> <bold>File not found</bold> at <cyan>/path/to/file</cyan>"
    rich_markup = "[red]Error:[/] [bold]File not found[/] at [cyan]/path/to/file[/]"
    
    # vargula
    vg_time = measure_time(
        lambda: vg.format(markup_text),
        iterations
    )
    
    # Rich
    rich_time = measure_time(
        lambda: console.render_str(rich_markup),
        iterations
    )
    
    print(f"vargula:  {vg_time:6.3f}ms")
    print(f"Rich:     {rich_time:6.3f}ms  ({rich_time/vg_time:5.1f}x)")
    print()


def benchmark_nested_tags():
    """Benchmark complex nested tag parsing"""
    print("=" * 70)
    print("4. NESTED TAGS BENCHMARK (2,000 iterations)")
    print("=" * 70)
    
    import vargula 
    vg = vargula.Vargula()
    from rich.console import Console
    
    console = Console(file=StringIO())
    iterations = 2000
    
    vg_nested = "<bold><red>Error: <italic>critical</italic> failure in <underline>module</underline></red></bold>"
    rich_nested = "[bold][red]Error: [italic]critical[/] failure in [underline]module[/][/][/]"
    
    # vargula
    vg_time = measure_time(
        lambda: vg.format(vg_nested),
        iterations
    )
    
    # Rich
    rich_time = measure_time(
        lambda: console.render_str(rich_nested),
        iterations
    )
    
    print(f"vargula:  {vg_time:6.3f}ms")
    print(f"Rich:     {rich_time:6.3f}ms  ({rich_time/vg_time:5.1f}x)")
    print()


def benchmark_hex_colors():
    """Benchmark hex color performance"""
    print("=" * 70)
    print("5. HEX COLOR BENCHMARK (5,000 iterations)")
    print("=" * 70)
    
    import vargula 
    vg = vargula.Vargula()
    from rich.console import Console
    
    console = Console(file=StringIO())
    iterations = 5000
    
    # vargula - hex foreground and background
    vg_time = measure_time(
        lambda: vg.format("<#FF5733>Orange text</#FF5733> <@#3498db>Blue background</@#3498db>"),
        iterations
    )
    
    # Rich - hex colors
    rich_time = measure_time(
        lambda: console.render_str("[#FF5733]Orange text[/] [on #3498db]Blue background[/]"),
        iterations
    )
    
    print(f"vargula:  {vg_time:6.3f}ms")
    print(f"Rich:     {rich_time:6.3f}ms  ({rich_time/vg_time:5.1f}x)")
    print()


def benchmark_table_creation():
    """Benchmark table creation and rendering"""
    print("=" * 70)
    print("6. TABLE CREATION BENCHMARK (500 iterations)")
    print("=" * 70)
    
    import vargula 
    vg = vargula.Vargula()
    from rich.console import Console
    from rich.table import Table as RichTable
    
    console = Console(file=StringIO())
    iterations = 500
    
    def create_vg_table():
        table = vg.Table(title="Users", style="cyan")
        table.add_column("Name", style="bold")
        table.add_column("Email", style="blue")
        table.add_column("Status", style="green")
        table.add_row("Alice", "alice@example.com", "Active")
        table.add_row("Bob", "bob@example.com", "Active")
        table.add_row("Charlie", "charlie@example.com", "Inactive")
        return str(table)
    
    def create_rich_table():
        table = RichTable(title="Users")
        table.add_column("Name", style="bold")
        table.add_column("Email", style="blue")
        table.add_column("Status", style="green")
        table.add_row("Alice", "alice@example.com", "Active")
        table.add_row("Bob", "bob@example.com", "Active")
        table.add_row("Charlie", "charlie@example.com", "Inactive")
        console.print(table)
    
    # vargula
    vg_time = measure_time(create_vg_table, iterations)
    
    # Rich
    rich_time = measure_time(create_rich_table, iterations)
    
    print(f"vargula:  {vg_time:6.3f}ms")
    print(f"Rich:     {rich_time:6.3f}ms  ({rich_time/vg_time:5.1f}x)")
    print()


def benchmark_color_manipulation():
    """Benchmark color manipulation operations"""
    print("=" * 70)
    print("7. COLOR MANIPULATION BENCHMARK (5,000 iterations)")
    print("=" * 70)
    
    import vargula 
    vg = vargula.Vargula()
    iterations = 5000
    
    def vg_color_ops():
        color = "#3498db"
        lighter = vg.lighten(color, 0.2)
        darker = vg.darken(color, 0.2)
        saturated = vg.saturate(color, 0.3)
        mixed = vg.mix(color, "#e74c3c", 0.5)
        return mixed
    
    # vargula (Rich doesn't have built-in color manipulation)
    vg_time = measure_time(vg_color_ops, iterations)
    
    print(f"vargula:  {vg_time:6.3f}ms")
    print("Rich:     N/A (no built-in color manipulation)")
    print()


def benchmark_palette_generation():
    """Benchmark palette generation"""
    print("=" * 70)
    print("8. PALETTE GENERATION BENCHMARK (1,000 iterations)")
    print("=" * 70)
    
    import vargula 
    vg = vargula.Vargula()
    iterations = 1000
    
    def generate_palettes():
        palette1 = vg.generate_palette("#3498db", "complementary", 5)
        palette2 = vg.generate_palette("#e74c3c", "analogous", 7)
        theme = vg.generate_theme_palette("triadic", "#9b59b6")
        return theme
    
    # vargula (Rich doesn't have palette generation)
    vg_time = measure_time(generate_palettes, iterations)
    
    print(f"vargula:  {vg_time:6.3f}ms")
    print("Rich:     N/A (no palette generation)")
    print()


def benchmark_accessibility():
    """Benchmark accessibility features"""
    print("=" * 70)
    print("9. ACCESSIBILITY BENCHMARK (2,000 iterations)")
    print("=" * 70)
    
    import vargula 
    vg = vargula.Vargula()
    iterations = 2000
    
    def accessibility_checks():
        ratio = vg.calculate_contrast_ratio("#FFFFFF", "#000000")
        meets = vg.meets_wcag("#3498db", "#FFFFFF", "AA")
        adjusted = vg.ensure_contrast("#888888", "#999999", 4.5)
        simulated = vg.simulate_colorblindness("#FF0000", "deuteranopia")
        return simulated
    
    # vargula (Rich doesn't have accessibility utilities)
    vg_time = measure_time(accessibility_checks, iterations)
    
    print(f"vargula:  {vg_time:6.3f}ms")
    print("Rich:     N/A (no accessibility utilities)")
    print()


def benchmark_real_world():
    """Benchmark real-world usage scenario"""
    print("=" * 70)
    print("10. REAL-WORLD SCENARIO BENCHMARK (1,000 iterations)")
    print("=" * 70)
    print("(Logging with multiple styled components)")
    print()
    
    import vargula 
    vg = vargula.Vargula()
    from rich.console import Console
    
    console = Console(file=StringIO())
    iterations = 1000
    
    def vg_logging():
        timestamp = vg.format("<dim>2024-11-22 10:30:45</dim>")
        level = vg.format("<@red><bold>ERROR</@red></bold>")
        message = vg.format("<red>Database connection failed</red>")
        details = vg.format("<cyan>host:</cyan> localhost <cyan>port:</cyan> 5432")
        return f"{timestamp} {level} {message} {details}"
    
    def rich_logging():
        return console.render_str(
            "[dim]2024-11-22 10:30:45[/] [bold on red]ERROR[/] "
            "[red]Database connection failed[/] [cyan]host:[/] localhost [cyan]port:[/] 5432"
        )
    
    # vargula
    vg_time = measure_time(vg_logging, iterations)
    
    # Rich
    rich_time = measure_time(rich_logging, iterations)
    
    print(f"vargula:  {vg_time:6.3f}ms")
    print(f"Rich:     {rich_time:6.3f}ms  ({rich_time/vg_time:5.1f}x)")
    print()


def print_summary():
    """Print benchmark summary"""
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("vargula excels at:")
    print("  ✓ Fast imports (minimal dependencies)")
    print("  ✓ Simple, intuitive tag syntax (<#hex>, <@background>)")
    print("  ✓ Built-in color manipulation (lighten, darken, mix, etc.)")
    print("  ✓ Palette generation with color theory")
    print("  ✓ Accessibility features (WCAG, colorblindness)")
    print("  ✓ Lightweight and fast for basic operations")
    print()
    print("Rich excels at:")
    print("  ✓ Complex layout rendering (panels, columns)")
    print("  ✓ Advanced progress bars with live updates")
    print("  ✓ Extensive box drawing and formatting")
    print("  ✓ Markdown and syntax highlighting")
    print("  ✓ Rich ecosystem and integrations")
    print()
    print("Use vargula when you need:")
    print("  • Fast, lightweight terminal styling")
    print("  • Color palette generation and manipulation")
    print("  • Accessibility-focused color tools")
    print("  • Simple markup-style formatting")
    print("  • Minimal import overhead")
    print()
    print("Use Rich when you need:")
    print("  • Complex terminal layouts and TUIs")
    print("  • Advanced rendering features")
    print("  • Markdown/syntax highlighting")
    print("  • Extensive styling options")
    print("=" * 70)


def main():
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "VARGULA COMPREHENSIVE BENCHMARK" + " " * 21 + "║")
    print("╚" + "═" * 68 + "╝")
    print()
    
    try:
        benchmark_imports()
        benchmark_basic_styling()
        benchmark_markup_parsing()
        benchmark_nested_tags()
        benchmark_hex_colors()
        benchmark_table_creation()
        benchmark_color_manipulation()
        benchmark_palette_generation()
        benchmark_accessibility()
        benchmark_real_world()
        print_summary()
        
    except ImportError as e:
        print(f"\n⚠️  Missing library: {e}")
        print("Install all dependencies: pip install vargula rich colorama")
    except Exception as e:
        print(f"\n❌ Benchmark error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()