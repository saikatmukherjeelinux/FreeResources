# ◈ DSA Motion Lab

**An interactive, animated Data Structures & Algorithms learning website.**

Understand algorithms by watching each operation, controlling playback, inspecting complexity, and reading runnable Python implementations.

## ✨ Features

- 🌌 Dark neon interface with responsive sidebar and smooth animated bars, nodes, graphs, and trees
- ▶️ Play / pause / previous / next controls, plus adjustable animation speed
- ✍️ Custom numeric inputs (up to 16 numbers) for most lessons
- 🐍 Read and copy complete Python examples
- 🧮 Explanations and time/space complexity notes
- 🧰 No framework, build system, CDN, Python dependency, or external font required
- 🧪 Python standard-library `unittest` suite

## 📚 Available interactive lessons

| Category | Lessons |
|---|---|
| Sorting | Bubble sort, Selection sort, Insertion sort |
| Searching | Linear search, Binary search |
| Linear structures | Stack, Queue, Singly linked list |
| Graphs | Breadth-first search (BFS), Depth-first search (DFS) |
| Trees | Binary search tree insertion |

**11 animated lessons included.** This is an extensible foundation, not an exhaustive implementation of every DSA topic.

## 🚀 Run locally

1. Download / clone this repository.
2. Open `index.html` in Chrome, Edge, Firefox, or Safari.

Optional local server (Python installed):

```bash
python -m http.server 8000
```

Visit `http://localhost:8000`.

Run the code samples:

```bash
python python_examples/algorithms.py
```

Run tests from the project root:

```bash
python -m unittest discover -s tests -v
```

## 📦 Project layout

```text
dsa-motion-lab/
├── index.html                # Learning studio
├── assets/
│   ├── style.css             # Responsive neon UI + transitions
│   └── app.js                # Lesson metadata + animation step engine
├── python_examples/
│   ├── __init__.py
│   └── algorithms.py         # Tested reference functions
├── tests/
│   └── test_algorithms.py
├── docs/
│   └── ROADMAP.md            # Suggested complete DSA curriculum
├── .gitignore
├── LICENSE
└── README.md
```

## 🌐 Publish with GitHub Pages

1. Create a **public** repository on GitHub (suggested name: `dsa-motion-lab`).
2. Upload these files, keeping the same folder structure.
3. Go to **Settings → Pages → Build and deployment**.
4. Choose **Deploy from a branch**, branch `main`, folder `/(root)`, then Save.
5. Your website will appear at `https://YOUR-USERNAME.github.io/dsa-motion-lab/` once GitHub deploys it.

If using Git locally:

```bash
git init
git add .
git commit -m "Launch animated DSA learning lab"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/dsa-motion-lab.git
git push -u origin main
```

Create the empty repository on GitHub before the final push. Replace `YOUR-USERNAME` with your own username.

## 🧠 Learning workflow

1. Read the concept and complexity.
2. Press **Next** to inspect the first operation.
3. Use **Play** to watch the full animation.
4. Read the Python implementation and run it locally.
5. Modify the input, predict the output, and compare your expectation.
6. Reimplement the algorithm yourself, then add tests.

## 🛣️ Expand the curriculum

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for an ordered curriculum covering Big O, arrays, recursion, hashing, heaps, trees, graphs, greedy, dynamic programming and advanced patterns.

## License

MIT. See [LICENSE](LICENSE).
