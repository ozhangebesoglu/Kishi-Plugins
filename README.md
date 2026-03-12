# Kishi Shell Plugin Marketplace

Welcome to the official marketplace for Kishi Shell! 🚀

Here you can build, collect, and share dynamic python-based plugins that seamlessly extend Kishi Shell.

## How to Install a Plugin
Inside a Kishi terminal, simply type:
```bash
plugin install <plugin-name>
```

For instance, to install the `hello` plugin from this repository:
```bash
plugin install hello
```

## How to Create a Plugin
Creating a plugin is extremely easy. Just create a `.py` file containing your command functions, and export them via a `PLUGIN_COMMANDS` dictionary at the bottom.

Example `my_command.py`:
```python
def example_function(args):
    print("This is a custom plugin output!")
    return 0
    
PLUGIN_COMMANDS = {
    "my_command": example_function
}
```

Then you can either upload it here or run `plugin install https://raw.github.../my_command.py`.
