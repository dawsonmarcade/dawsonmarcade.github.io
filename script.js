function goToProject() {
    const projectURL = "https://github.com/dawsonmarcade/dawsonmarcade.github.io/tree/main/monte_carlo_simulator";
    window.location.href = projectURL;
}



/// code for dark mode button toggle
const toggleButton = document.getElementById('themeToggle');
const bodyElement = document.body;

toggleButton.addEventListener('click', () => {
    // toggle dark mode logic
    const currentTheme = document.documentElement.getAttribute('data-theme');
    // check if current theme is light, ? will make it dark if its light and light if its dark
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';

    document.documentElement.setAttribute('data-theme', newTheme)
    localStorage.setItem('theme', newTheme)

})