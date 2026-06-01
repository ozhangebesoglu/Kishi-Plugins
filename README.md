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

## How to Create a Plugin (For Developers)

Creating a plugin is extremely easy. Just create a `.py` file containing your command functions, and export them via a `PLUGIN_COMMANDS` dictionary at the bottom.

**CRITICAL RULE:** To make it easy for users, your plugin's filename **MUST exactly match** the command name it exports (e.g., `weather.py` must export `"weather"`).

Example `my_command.py`:
```python
def my_custom_function(args):
    print("This is a custom plugin output!")
    return 0
    
PLUGIN_COMMANDS = {
    # This key MUST match the file name (my_command.py -> "my_command")
    "my_command": my_custom_function
}
```

Then you can either upload it to this repository or run `plugin install https://raw.github.../my_command.py`.

---

## What's New in Kishi Shell v2.0.2.0

The latest Kishi release ships major upgrades to **Krep AI** — Kishi's
built-in 3D semantic search tool. None of this changes the plugin API;
existing plugins keep working exactly as before. But your plugins can now
take advantage of a much smarter semantic engine.

### 1. Krep is now a standalone CLI

`pip install kishi-shell` now installs two binaries: `kishi` and `krep`.
Your plugins can shell out to `krep` from any environment (bash, zsh,
fish), not just inside the Kishi REPL.

```bash
$ krep "auth login" /var/log/         # works from any shell
$ cat app.log | krep error
```

### 2. ripgrep streaming prefilter (150-3000× speedup)

If `rg` is installed on the system, Krep automatically uses it as a
line-level prefilter and only vectorizes matching lines. Falls back to
the built-in Python walker if `rg` is missing or for stdin input. Zero
configuration on your end.

Benchmark (3-run averages):
- Kishi src (~5k lines), `auth login`:  1668 ms → **5 ms**  (220×)
- Python stdlib (6.8M lines):            timeout → **11 ms** (>5000×)
- 1 GB single file (17M lines):          timeout → **6 ms** (>10000×)

### 3. Dictionary-free LSA model (optional)

`krep --learn /var/log/` trains a per-corpus PPMI + SVD model. Vocabulary,
axes, and word vectors are learned from the actual files — no manual
dictionary, multilingual by construction.

```bash
krep --learn /var/log/ --auto-refresh 1h    # build + auto-refresh hourly
krep --update-learn /var/log/                # manual tail-only update
krep --list-models                           # show cached models
krep "auth failure" /var/log/                # auto-uses model if present
```

The LSA model requires `numpy` + `scipy` as **optional dependencies**:
```bash
pip install "kishi-shell[krep]"   # adds numpy + scipy
# or on Arch:
sudo pacman -S python-numpy python-scipy
```

The base install stays at the original 2 dependencies (`prompt_toolkit`,
`psutil`). Keyword-based krep works without the extras.

### 4. Tail-aware incremental + lazy auto-refresh

Log files are append-only; Krep tracks each file's last-read byte offset.
With `--auto-refresh INTERVAL`, every query checks the model age and
fires a **background subprocess** to refresh it if stale. No daemon, no
cron — fire-and-forget. Useful if your plugin shells out to `krep` on
log files that are constantly being written.

### Plugin author guidance

You don't need to change anything. But if your plugin does its own
log/file search, consider piping through `krep` for free semantic
ranking and 3D scatter visualization:

```python
import subprocess, sys
def mysearch(args):
    query = " ".join(args[1:])
    rc = subprocess.call(["krep", query, "/var/log/", "-l", "10"])
    return rc

PLUGIN_COMMANDS = {"mysearch": mysearch}
```

More details in the main repo: https://github.com/ozhangebesoglu/Kishi-Shell
