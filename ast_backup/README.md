# Asteroids Game

An interactive, retro-style **Asteroids** arcade game clone built with **Python 3.13+** and **Pygame 2.6**. 

This project was built as part of the Boot.dev career track to learn the fundamentals of object-oriented programming (OOP), collision detection, game loops, vector math, and 2D sprite rendering.

---

## 🎮 Gameplay & Controls

Control your triangular spaceship to navigate through a dense asteroid field, shooting down asteroids to survive!

- **`W`**: Move forward (Thrust)
- **`S`**: Move backward
- **`A`**: Rotate Counter-Clockwise (Turn Left)
- **`D`**: Rotate Clockwise (Turn Right)
- **`SPACE`**: Shoot lasers

*The game ends immediately if an asteroid collides with your ship.*

---

## 🚀 Getting Started

### Prerequisites

You need **Python 3.13 or newer** installed on your system. 

It is highly recommended to use [uv](https://github.com/astral-sh/uv), a fast Python package installer and resolver.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kouroshtkk/asteroids.git
   cd asteroids
   ```

2. **Set up the virtual environment & install dependencies:**

   **Using `uv` (Recommended):**
   ```bash
   uv sync
   ```

   **Using standard `pip`:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r pyproject.toml
   ```

### Running the Game

To start the game:

**Using `uv`:**
```bash
uv run main.py
```

**Using standard Python:**
```bash
python main.py
```

---

## 🛠️ How to Create an Executable (For distribution)

You can package this game into a standalone executable so others can play it without needing to install Python or Pygame.

We recommend using **PyInstaller**. Since executables are platform-dependent, you must build the executable on the operating system you target (e.g., build on Windows to get a `.exe`, build on macOS to get an app/executable).

### Step 1: Install PyInstaller

Install PyInstaller in your project environment:

**Using `uv`:**
```bash
uv pip install pyinstaller
```

**Using standard `pip` (within your activated virtual environment):**
```bash
pip install pyinstaller
```

### Step 2: Build the Executable

Run the following command to generate a single executable file:

```bash
# On Linux / macOS:
pyinstaller --onefile --windowed --name "Asteroids" main.py

# On Windows:
pyinstaller --onefile --windowed --name "Asteroids" --icon=NONE main.py
```

#### Flags used:
- `--onefile`: Packages the entire game and Python runtime into a single executable file.
- `--windowed` (or `-w`): Prevents a console/terminal window from opening in the background when running the game.
- `--name "Asteroids"`: Sets the name of the output executable.

### Step 3: Distribute

After the build process completes successfully:
1. Locate your standalone executable inside the newly created `dist/` directory.
2. Share the executable from the `dist/` folder with friends!

---

## 🔍 Features & Codebase Architecture

- **Vector Mathematics:** Real-time directional calculations, rotation, and velocities utilizing `pygame.Vector2`.
- **Custom Collision Engine:** Simplified circle-collision algorithms ([circleshape.py](file:///home/kouroshtkk/bootdev/asteroids/circleshape.py)) for efficient hitbox checks between player, shots, and asteroids.
- **Dynamic Spawning:** An automated `AsteroidField` ([asteroidfield.py](file:///home/kouroshtkk/bootdev/asteroids/asteroidfield.py)) system that dynamically spawns and routes incoming asteroids of varying sizes.
- **State Logging:** Automatically records frame logs of the player's coordinate vectors, current velocities, active sprites, and game events (e.g., collisions, shots fired) using a dedicated logger ([logger.py](file:///home/kouroshtkk/bootdev/asteroids/logger.py)) to:
  - `game_state.jsonl` (frame snapshot metrics)
  - `game_events.jsonl` (milestone event triggers)
  These files are generated locally and ignored by Git.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
