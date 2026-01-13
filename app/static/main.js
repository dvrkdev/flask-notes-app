const html = document.documentElement;
const toggleBtn = document.getElementById("themeToggle");
const icon = toggleBtn.querySelector("i");

const saved = localStorage.getItem("theme") || "dark";
setTheme(saved);

toggleBtn.addEventListener("click", () => {
    const next = html.dataset.bsTheme === "dark" ? "light" : "dark";
    setTheme(next);
});

function setTheme(theme) {
    html.dataset.bsTheme = theme;
    localStorage.setItem("theme", theme);
    icon.className = theme === "dark"
        ? "bi bi-moon"
        : "bi bi-sun";
}