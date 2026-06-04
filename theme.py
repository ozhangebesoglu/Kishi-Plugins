"""
theme — Kishi color theme switcher.

Requires: Kishi Shell v2.0.2.4+ (kishi.themes module).

Usage:
  theme                # list themes, mark active
  theme list           # = default
  theme current        # print active theme name
  theme get            # = current
  theme set NAME       # switch theme (writes ~/.config/kishi/theme)
                       # restart Kishi to apply

Available themes: monokai, dracula, one-dark, solarized-dark, solarized-light.
"""


def theme(args):
    color_green = "\033[1;32m"
    color_red = "\033[1;31m"
    color_amber = "\033[38;2;255;191;0m"
    color_cyan = "\033[1;36m"
    color_reset = "\033[0m"

    try:
        from kishi import themes
    except ImportError:
        print(f"{color_red}theme plugin requires Kishi Shell v2.0.2.4+{color_reset}")
        print("  Upgrade: pip install --upgrade kishi-shell")
        return 1

    if len(args) < 2 or args[1] == "list":
        current = themes.get_current_theme()
        print(f"{color_amber}Kishi Themes{color_reset}")
        for name in themes.list_themes():
            marker = f" {color_green}(active){color_reset}" if name == current else ""
            print(f"  - {name}{marker}")
        print()
        print(f"Use: {color_cyan}theme set NAME{color_reset} "
              f"(restart Kishi to apply)")
        return 0

    action = args[1].lower()

    if action in ("current", "get"):
        print(themes.get_current_theme())
        return 0

    if action == "set":
        if len(args) < 3:
            print(f"{color_red}Usage: theme set NAME{color_reset}")
            print(f"Available: {', '.join(themes.list_themes())}")
            return 1
        name = args[2]
        try:
            themes.set_current_theme(name)
        except ValueError as e:
            print(f"{color_red}{e}{color_reset}")
            return 1
        print(f"{color_green}[+]{color_reset} Theme set to: "
              f"{color_cyan}{name}{color_reset}")
        print(f"    Restart Kishi to apply (themes load at startup).")
        return 0

    print(f"{color_red}Unknown action: {action}{color_reset}")
    print(f"Usage: theme [list|current|set NAME]")
    return 1


PLUGIN_COMMANDS = {
    "theme": theme,
}
