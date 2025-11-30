import vargula
import sys
import tty
import termios

vg = vargula.Vargula()

def get_key():
    """Get a single keypress from the user."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        # Handle escape sequences for arrow keys
        if ch == '\x1b':
            ch = sys.stdin.read(2)
            if ch == '[A':
                return 'up'
            elif ch == '[B':
                return 'down'
            elif ch == '[C':
                return 'right'
            elif ch == '[D':
                return 'left'
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def clear_screen():
    """Clear the terminal screen."""
    print("\033[2J\033[H", end='')

def render_menu(title, items, selected_index, header_color="#00d9ff", 
                item_color="#00ff88", selected_bg="#00ff88", disabled_color="#666666"):
    """
    Render an interactive menu.
    
    Args:
        title: Menu title
        items: List of tuples (item_name, enabled)
        selected_index: Currently selected item index
        header_color: Color for the title/header
        item_color: Color for menu items
        selected_bg: Background color for selected item
        disabled_color: Color for disabled items
    """
    # Create styles
    vg.create("menu_title", color=header_color, look="bold")
    vg.create("menu_item", color=item_color)
    vg.create("menu_selected", color="black", bg=selected_bg, look="bold")
    vg.create("menu_disabled", color=disabled_color)
    
    # Calculate box width
    max_item_len = max(len(item[0]) for item in items)
    box_width = max(len(title) + 4, max_item_len + 6)
    
    # Render header
    top_border = "╔" + "═" * (box_width - 2) + "╗"
    title_line = "║" + title.center(box_width - 2) + "║"
    bottom_border = "╚" + "═" * (box_width - 2) + "╝"
    
    print(vg.format(f"<menu_title>{top_border}</menu_title>"))
    print(vg.format(f"<menu_title>{title_line}</menu_title>"))
    print(vg.format(f"<menu_title>{bottom_border}</menu_title>"))
    print()
    
    # Render menu items
    for i, (item_name, enabled) in enumerate(items):
        if i == selected_index:
            # Selected item
            arrow = "→"
            padded_item = f" {arrow} {item_name}".ljust(box_width)
            print(vg.format(f"<menu_selected>{padded_item}</menu_selected>"))
        elif not enabled:
            # Disabled item
            padded_item = f"   {item_name}".ljust(box_width)
            print(vg.format(f"<menu_disabled>{padded_item}</menu_disabled>"))
        else:
            # Normal item
            padded_item = f"   {item_name}".ljust(box_width)
            print(vg.format(f"<menu_item>{padded_item}</menu_item>"))

def interactive_menu(title, items, header_color="#00d9ff", item_color="#00ff88", 
                     selected_bg="#00ff88", disabled_color="#666666"):
    """
    Display an interactive menu with keyboard navigation.
    
    Args:
        title: Menu title
        items: List of tuples (item_name, enabled)
        header_color: Color for the title/header
        item_color: Color for menu items
        selected_bg: Background color for selected item
        disabled_color: Color for disabled items
        
    Returns:
        Index of selected item or None if cancelled
    """
    selected = 0
    
    # Find first enabled item
    for i, (_, enabled) in enumerate(items):
        if enabled:
            selected = i
            break
    
    while True:
        clear_screen()
        render_menu(title, items, selected, header_color, item_color, selected_bg, disabled_color)
        
        print()
        print(vg.format("<menu_disabled>Use ↑/↓ arrows to navigate, Enter to select, 'q' to quit</menu_disabled>"))
        
        key = get_key()
        
        if key == 'up':
            # Move up to previous enabled item
            new_selected = selected - 1
            while new_selected >= 0:
                if items[new_selected][1]:  # Check if enabled
                    selected = new_selected
                    break
                new_selected -= 1
        
        elif key == 'down':
            # Move down to next enabled item
            new_selected = selected + 1
            while new_selected < len(items):
                if items[new_selected][1]:  # Check if enabled
                    selected = new_selected
                    break
                new_selected += 1
        
        elif key == '\r' or key == '\n':  # Enter key
            if items[selected][1]:  # Only select if enabled
                clear_screen()
                return selected
        
        elif key == 'q' or key == 'Q':
            clear_screen()
            return None

# Example usage
if __name__ == "__main__":
    # Define menu items as (name, enabled)
    menu_items = [
        ("New Project", True),
        ("Open Project", True),
        ("Recent Files", True),
        ("Settings", True),
        ("Export (Not Available)", False),
        ("Exit", True),
    ]
    
    result = interactive_menu("MAIN MENU", menu_items)
    
    if result is not None:
        print(vg.format(f"<menu_item>You selected: {menu_items[result][0]}</menu_item>"))
    else:
        print(vg.format("<menu_disabled>Menu cancelled</menu_disabled>"))