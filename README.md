# MiDeck 🎛️

**MiDeck** is a small Python macro deck that turns a MIDI controller into a programmable shortcut pad.

The idea is simple: press a MIDI key/pad → MiDeck receives the MIDI note → looks up the corresponding action in `config.json` → executes the Python function.

> 🚧 Early-stage project — the current example is configured to launch Steam on Windows, but the mapping system is designed to be extended with your own actions.

## ✨ Features

* 🎹 Listen for MIDI `note_on` and `note_off` events
* 🗺️ Map MIDI notes to Python functions through a JSON config
* 🐍 Define custom actions in `func.py`
* 🔌 Detect connected MIDI input devices
* 🪟 Designed with Windows automation in mind

## 📁 Project structure

```text
mideck/
├── main.py       # MIDI listener and action dispatcher
├── func.py       # Custom actions
├── config.json   # MIDI note → action mappings
├── README.md
└── LICENSE
```

## 🚀 Installation

### Requirements

* Python 3.x
* A MIDI controller/device
* Python packages:

  * [Mido](https://mido.readthedocs.io/)
  * [python-rtmidi](https://pypi.org/project/python-rtmidi/)
  * [Lupa](https://pypi.org/project/lupa/)

Install the dependencies with:

```bash
pip install mido python-rtmidi lupa
```

## ▶️ Usage

Connect your MIDI controller, then run:

```bash
python main.py
```

MiDeck will print the MIDI input devices it detects:

```text
Detected devices
Input: Your MIDI Controller
```

It will then listen for MIDI messages.

When a mapped note is pressed, the corresponding function from `func.py` is called.

## ⚙️ Configuration

Mappings are stored in `config.json`.

For example:

```json
{
    "devices": "",
    "mappings": {
        "60": "open_steam"
    }
}
```

Here, MIDI note **60** (Middle C / C4) is mapped to the `open_steam` function.

### Adding a new action

Add a function to `func.py`:

```python
def open_calculator():
    # your action here
    pass
```

Then map a MIDI note to it:

```json
{
    "devices": "",
    "mappings": {
        "60": "open_steam",
        "61": "open_calculator"
    }
}
```

That's it — pressing note 61 will call `open_calculator()`.

## 🧩 How it works

The main loop follows a simple pipeline:

```text
MIDI Controller
      │
      ▼
   main.py
      │
      ▼
  MIDI note
      │
      ▼
 config.json
      │
      ▼
 Python function
      │
      ▼
    Action
```

When a `note_on` event is received, MiDeck:

1. Reads the MIDI note number.
2. Looks for that note in `config.json`.
3. Retrieves the function name.
4. Finds the function in `func.py`.
5. Executes it.

If a note isn't mapped, it is simply ignored.

## 🪟 Windows example

The current `open_steam()` example launches Steam using its default installation path:

```python
def open_steam():
    subprocess.call("C:\\Program Files (x86)\\Steam\\steam.exe")
```

If Steam is installed somewhere else, update the path in `func.py`.

You can use the same approach to launch applications, scripts, tools, or other local commands.

##

## 📄 License

MiDeck is released under the **MIT License**. See [LICENSE](LICENSE) for details.

---

Made with 🎹 + 🐍 by [JulioLeGrandSage](https://github.com/juliolegrandsage).

```

Petit détail au passage : ton `main.py` importe **Lupa** mais ne l'utilise pas encore, donc j'ai gardé la dépendance dans le README pour refléter le code actuel.
```
