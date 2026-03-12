def hello_plugin(args):
    # This color constant is from Kishi's core engine
    color_green = "\033[32m"
    color_reset = "\033[0m"
    
    print(f"{color_green}Hello! I am downloading from your brand new Kishi-Plugins GitHub Marketplace!{color_reset}")
    return 0

PLUGIN_COMMANDS = {
    "hello": hello_plugin
}
