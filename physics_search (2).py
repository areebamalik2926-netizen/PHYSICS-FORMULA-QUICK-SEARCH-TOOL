import tkinter as tk
from tkinter import ttk

FORMULAS = [
    {
        "name": "Newton's Second Law",
        "formula": "F = m x a",
        "topic": "Mechanics",
        "variables": "F = Force (N)  |  m = mass (kg)  |  a = acceleration (m/s2)",
        "keywords": ["force", "mass", "acceleration", "newton", "mechanics"],
    },
    {
        "name": "Velocity",
        "formula": "v = d / t",
        "topic": "Mechanics",
        "variables": "v = velocity (m/s)  |  d = distance (m)  |  t = time (s)",
        "keywords": ["velocity", "speed", "distance", "time", "mechanics"],
    },
    {
        "name": "Acceleration",
        "formula": "a = (v - u) / t",
        "topic": "Mechanics",
        "variables": "a = acceleration (m/s2)  |  v = final velocity  |  u = initial velocity  |  t = time (s)",
        "keywords": ["acceleration", "velocity", "mechanics"],
    },
    {
        "name": "Momentum",
        "formula": "p = m x v",
        "topic": "Mechanics",
        "variables": "p = momentum (kg.m/s)  |  m = mass (kg)  |  v = velocity (m/s)",
        "keywords": ["momentum", "mass", "velocity", "mechanics"],
    },
    {
        "name": "Weight",
        "formula": "W = m x g",
        "topic": "Mechanics",
        "variables": "W = weight (N)  |  m = mass (kg)  |  g = gravity (9.8 m/s2)",
        "keywords": ["weight", "gravity", "mass", "mechanics"],
    },
    {
        "name": "Friction Force",
        "formula": "f = u x N",
        "topic": "Mechanics",
        "variables": "f = friction force (N)  |  u = coefficient of friction  |  N = normal force (N)",
        "keywords": ["friction", "normal", "mechanics"],
    },
    {
        "name": "Pressure",
        "formula": "P = F / A",
        "topic": "Mechanics",
        "variables": "P = pressure (Pa)  |  F = force (N)  |  A = area (m2)",
        "keywords": ["pressure", "force", "area", "mechanics"],
    },
    {
        "name": "Density",
        "formula": "p = m / V",
        "topic": "Mechanics",
        "variables": "p = density (kg/m3)  |  m = mass (kg)  |  V = volume (m3)",
        "keywords": ["density", "mass", "volume", "mechanics"],
    },
    {
        "name": "Kinetic Energy",
        "formula": "KE = 0.5 x m x v^2",
        "topic": "Energy",
        "variables": "KE = kinetic energy (J)  |  m = mass (kg)  |  v = velocity (m/s)",
        "keywords": ["kinetic", "energy", "velocity", "mass"],
    },
    {
        "name": "Potential Energy",
        "formula": "PE = m x g x h",
        "topic": "Energy",
        "variables": "PE = potential energy (J)  |  m = mass (kg)  |  g = 9.8 m/s2  |  h = height (m)",
        "keywords": ["potential", "energy", "gravity", "height"],
    },
    {
        "name": "Work Done",
        "formula": "W = F x d x cos(angle)",
        "topic": "Energy",
        "variables": "W = work (J)  |  F = force (N)  |  d = displacement (m)  |  angle = direction",
        "keywords": ["work", "force", "displacement", "energy"],
    },
    {
        "name": "Power",
        "formula": "P = W / t",
        "topic": "Energy",
        "variables": "P = power (W)  |  W = work (J)  |  t = time (s)",
        "keywords": ["power", "work", "time", "energy"],
    },
    {
        "name": "Efficiency",
        "formula": "Eff = (useful output / total input) x 100%",
        "topic": "Energy",
        "variables": "Eff = efficiency (%)  |  output and input in same units (J or W)",
        "keywords": ["efficiency", "energy", "output", "input"],
    },
    {
        "name": "Wave Speed",
        "formula": "v = f x wavelength",
        "topic": "Waves",
        "variables": "v = wave speed (m/s)  |  f = frequency (Hz)  |  wavelength in (m)",
        "keywords": ["wave", "speed", "frequency", "wavelength"],
    },
    {
        "name": "Frequency and Period",
        "formula": "f = 1 / T",
        "topic": "Waves",
        "variables": "f = frequency (Hz)  |  T = period (s)",
        "keywords": ["frequency", "period", "wave"],
    },
    {
        "name": "Snell's Law",
        "formula": "n1 x sin(A1) = n2 x sin(A2)",
        "topic": "Waves",
        "variables": "n = refractive index  |  A = angle of incidence or refraction",
        "keywords": ["snell", "refraction", "light", "wave", "optics"],
    },
    {
        "name": "Refractive Index",
        "formula": "n = c / v",
        "topic": "Waves",
        "variables": "n = refractive index  |  c = speed of light (3x10^8 m/s)  |  v = speed in medium",
        "keywords": ["refractive", "index", "light", "optics", "wave"],
    },
    {
        "name": "Ohm's Law",
        "formula": "V = I x R",
        "topic": "Electricity",
        "variables": "V = voltage (V)  |  I = current (A)  |  R = resistance (Ohm)",
        "keywords": ["ohm", "voltage", "current", "resistance", "electricity"],
    },
    {
        "name": "Electrical Power",
        "formula": "P = V x I",
        "topic": "Electricity",
        "variables": "P = power (W)  |  V = voltage (V)  |  I = current (A)",
        "keywords": ["power", "voltage", "current", "electricity"],
    },
    {
        "name": "Electrical Energy",
        "formula": "E = P x t",
        "topic": "Electricity",
        "variables": "E = energy (J)  |  P = power (W)  |  t = time (s)",
        "keywords": ["energy", "power", "time", "electricity"],
    },
    {
        "name": "Charge",
        "formula": "Q = I x t",
        "topic": "Electricity",
        "variables": "Q = charge (C)  |  I = current (A)  |  t = time (s)",
        "keywords": ["charge", "current", "time", "electricity"],
    },
    {
        "name": "Resistors in Series",
        "formula": "R_total = R1 + R2 + R3 ...",
        "topic": "Electricity",
        "variables": "R_total = total resistance (Ohm)  |  R1, R2 = individual resistors",
        "keywords": ["series", "resistance", "resistor", "electricity"],
    },
    {
        "name": "Resistors in Parallel",
        "formula": "1/R_total = 1/R1 + 1/R2 ...",
        "topic": "Electricity",
        "variables": "R_total = total resistance (Ohm)  |  R1, R2 = individual resistors",
        "keywords": ["parallel", "resistance", "resistor", "electricity"],
    },
    {
        "name": "Ideal Gas Law",
        "formula": "PV = nRT",
        "topic": "Thermodynamics",
        "variables": "P = pressure (Pa)  |  V = volume (m3)  |  n = moles  |  R = 8.314  |  T = temperature (K)",
        "keywords": ["ideal", "gas", "pressure", "volume", "temperature", "thermodynamics"],
    },
    {
        "name": "Heat Energy",
        "formula": "Q = m x c x dT",
        "topic": "Thermodynamics",
        "variables": "Q = heat (J)  |  m = mass (kg)  |  c = specific heat capacity  |  dT = temp change (K)",
        "keywords": ["heat", "temperature", "specific heat", "thermodynamics"],
    },
    {
        "name": "Thermal Expansion",
        "formula": "dL = a x L0 x dT",
        "topic": "Thermodynamics",
        "variables": "dL = change in length  |  a = expansion coefficient  |  L0 = original length  |  dT = temp change",
        "keywords": ["thermal", "expansion", "length", "temperature", "thermodynamics"],
    },
    {
        "name": "Universal Gravitation",
        "formula": "F = G x (m1 x m2) / r^2",
        "topic": "Gravitation",
        "variables": "F = force (N)  |  G = 6.67x10^-11  |  m1, m2 = masses (kg)  |  r = distance (m)",
        "keywords": ["gravity", "gravitation", "universal", "force", "mass"],
    },
    {
        "name": "Gravitational PE",
        "formula": "U = -G x m1 x m2 / r",
        "topic": "Gravitation",
        "variables": "U = gravitational PE (J)  |  G = 6.67x10^-11  |  m = masses (kg)  |  r = distance (m)",
        "keywords": ["gravitational", "potential", "energy", "gravitation"],
    },
    {
        "name": "Centripetal Force",
        "formula": "F = m x v^2 / r",
        "topic": "Circular Motion",
        "variables": "F = centripetal force (N)  |  m = mass (kg)  |  v = speed (m/s)  |  r = radius (m)",
        "keywords": ["centripetal", "circular", "force", "radius"],
    },
    {
        "name": "Centripetal Acceleration",
        "formula": "a = v^2 / r",
        "topic": "Circular Motion",
        "variables": "a = acceleration (m/s2)  |  v = speed (m/s)  |  r = radius (m)",
        "keywords": ["centripetal", "acceleration", "circular", "radius"],
    },
]

ALL_TOPICS = sorted(set(f["topic"] for f in FORMULAS))


def search_formulas(query, topic_filter="All"):
    query = query.lower().strip()
    results = []
    for f in FORMULAS:
        if topic_filter != "All" and f["topic"] != topic_filter:
            continue
        if (query == ""
                or any(query in kw for kw in f["keywords"])
                or query in f["name"].lower()
                or query in f["formula"].lower()):
            results.append(f)
    return results


class PhysicsSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Physics Formula Quick Search")
        self.root.geometry("900x680")
        self.root.resizable(True, True)
        self.root.configure(bg="#0d1117")
        self.active_topic = tk.StringVar(value="All")
        self._build_ui()
        self._show_results(FORMULAS)

    def _build_ui(self):

        header = tk.Frame(self.root, bg="#0d1117", pady=16)
        header.pack(fill="x", padx=30)

        tk.Label(
            header,
            text="Physics Formula Quick Search",
            font=("Helvetica", 22, "bold"),
            fg="#58d68d",
            bg="#0d1117",
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Type a keyword  |  filter by topic  |  instant results",
            font=("Helvetica", 10),
            fg="#555577",
            bg="#0d1117",
        ).pack(anchor="w", pady=(2, 0))

        info_frame = tk.Frame(self.root, bg="#161b22", pady=10, padx=20)
        info_frame.pack(fill="x", padx=30, pady=(0, 6))

        tk.Label(
            info_frame,
            text="Amina Fida   |   Areeba Adeel",
            font=("Helvetica", 11, "bold"),
            fg="#58d68d",
            bg="#161b22",
        ).pack(anchor="w")

        tk.Label(
            info_frame,
            text="Department of Physics and Applied Mathematics",
            font=("Helvetica", 10),
            fg="#8b949e",
            bg="#161b22",
        ).pack(anchor="w")

        tk.Label(
            info_frame,
            text="Pakistan Institute of Engineering and Applied Sciences",
            font=("Helvetica", 10),
            fg="#8b949e",
            bg="#161b22",
        ).pack(anchor="w")

        search_frame = tk.Frame(self.root, bg="#161b22", pady=10, padx=16)
        search_frame.pack(fill="x", padx=30, pady=(0, 8))

        tk.Label(
            search_frame,
            text="Search:",
            font=("Helvetica", 12, "bold"),
            bg="#161b22",
            fg="#58d68d",
        ).pack(side="left")

        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda *_: self._on_search())

        entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Helvetica", 13),
            bg="#21262d",
            fg="#e6edf3",
            insertbackground="#58d68d",
            relief="flat",
            bd=4,
        )
        entry.pack(side="left", fill="x", expand=True, padx=10, ipady=5)
        entry.focus_set()

        tk.Button(
            search_frame,
            text="Clear",
            font=("Helvetica", 10),
            bg="#21262d",
            fg="#8b949e",
            relief="flat",
            cursor="hand2",
            command=self._clear_search,
        ).pack(side="right")

        filter_frame = tk.Frame(self.root, bg="#0d1117")
        filter_frame.pack(fill="x", padx=30, pady=(0, 8))

        tk.Label(
            filter_frame,
            text="Filter: ",
            font=("Helvetica", 10),
            bg="#0d1117",
            fg="#555577",
        ).pack(side="left")

        topics = ["All"] + ALL_TOPICS
        self.filter_buttons = {}
        for topic in topics:
            btn = tk.Button(
                filter_frame,
                text=topic,
                font=("Helvetica", 9, "bold"),
                relief="flat",
                cursor="hand2",
                padx=8,
                pady=3,
                command=lambda t=topic: self._set_topic(t),
            )
            btn.pack(side="left", padx=2)
            self.filter_buttons[topic] = btn

        self._update_filter_buttons()

        self.count_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 9),
            fg="#555577",
            bg="#0d1117",
            anchor="w",
        )
        self.count_label.pack(fill="x", padx=34, pady=(0, 4))

        canvas_frame = tk.Frame(self.root, bg="#0d1117")
        canvas_frame.pack(fill="both", expand=True, padx=30, pady=(0, 16))

        self.canvas = tk.Canvas(canvas_frame, bg="#0d1117", highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.results_frame = tk.Frame(self.canvas, bg="#0d1117")
        self.canvas_window = self.canvas.create_window((0, 0), window=self.results_frame, anchor="nw")

        self.results_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel_mac)

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def _on_mousewheel_mac(self, event):
        self.canvas.yview_scroll(int(-1 * event.delta), "units")

    def _on_search(self):
        results = search_formulas(self.search_var.get(), self.active_topic.get())
        self._show_results(results)

    def _set_topic(self, topic):
        self.active_topic.set(topic)
        self._update_filter_buttons()
        self._on_search()

    def _clear_search(self):
        self.search_var.set("")

    def _update_filter_buttons(self):
        active = self.active_topic.get()
        for topic, btn in self.filter_buttons.items():
            if topic == active:
                btn.config(bg="#58d68d", fg="#0d1117")
            else:
                btn.config(bg="#21262d", fg="#8b949e")

    def _show_results(self, results):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        count = len(results)
        self.count_label.config(
            text="  {} formula{} found".format(count, "s" if count != 1 else "")
        )

        if not results:
            tk.Label(
                self.results_frame,
                text="No formulas found.\nTry: force  energy  wave  ohm  velocity",
                font=("Helvetica", 12),
                fg="#555577",
                bg="#0d1117",
                justify="center",
                pady=60,
            ).pack(fill="x")
            return

        for formula in results:
            self._render_card(formula)

    def _render_card(self, formula):
        topic_colors = {
            "Mechanics":       "#e67e22",
            "Energy":          "#f1c40f",
            "Waves":           "#3498db",
            "Electricity":     "#9b59b6",
            "Thermodynamics":  "#e74c3c",
            "Gravitation":     "#1abc9c",
            "Circular Motion": "#2ecc71",
        }
        color = topic_colors.get(formula["topic"], "#58d68d")

        card = tk.Frame(self.results_frame, bg="#161b22", pady=12, padx=16)
        card.pack(fill="x", pady=4, padx=2)

        tk.Frame(card, bg=color, width=5).pack(side="left", fill="y", padx=(0, 12))

        content = tk.Frame(card, bg="#161b22")
        content.pack(side="left", fill="both", expand=True)

        top_row = tk.Frame(content, bg="#161b22")
        top_row.pack(fill="x")

        tk.Label(
            top_row,
            text=formula["name"],
            font=("Helvetica", 13, "bold"),
            fg="#e6edf3",
            bg="#161b22",
            anchor="w",
        ).pack(side="left")

        tk.Label(
            top_row,
            text="  [{}]".format(formula["topic"]),
            font=("Helvetica", 9),
            fg=color,
            bg="#161b22",
        ).pack(side="left")

        tk.Label(
            content,
            text=formula["formula"],
            font=("Courier New", 15, "bold"),
            fg=color,
            bg="#161b22",
            anchor="w",
            pady=5,
        ).pack(fill="x")

        tk.Frame(content, bg="#21262d", height=1).pack(fill="x", pady=3)

        tk.Label(
            content,
            text=formula["variables"],
            font=("Helvetica", 9),
            fg="#8b949e",
            bg="#161b22",
            anchor="w",
            wraplength=700,
            justify="left",
        ).pack(fill="x")


if __name__ == "__main__":
    root = tk.Tk()
    app = PhysicsSearchApp(root)
    root.mainloop()
