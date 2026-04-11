function generatePattern() {
    const type = document.getElementById('patternType').value;
    const symbol = document.getElementById('symbol').value || '*';
    const rows = parseInt(document.getElementById('rows').value);
    const outputDiv = document.getElementById('output');
    let result = "";

    if (type === "full") {
        // Full Pyramid Logic: Perfect centering
        for (let i = 1; i <= rows; i++) {
            // Formula for leading spaces: Total Rows - Current Row
            let spaces = " ".repeat(rows - i);
            // Symbol followed by a space repeated 'i' times
            let stars = (symbol + " ").repeat(i);
            result += spaces + stars + "\n";
        }
    } else {
        // Inverted Half Pyramid Logic: Left aligned
        for (let i = rows; i >= 1; i--) {
            result += (symbol + " ").repeat(i).trimEnd() + "\n";
        }
    }

    outputDiv.innerText = result;
}