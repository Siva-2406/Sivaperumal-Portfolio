
function toggleTheme() {
    document.body.classList.toggle("dark-mode");
}

function calculate() {
    let amount = parseFloat(document.getElementById('amount').value) || 0;
    let rate = parseFloat(document.getElementById('rate').value) || 0;
    let years = parseFloat(document.getElementById('years').value) || 0;
    
    if (amount === 0 || rate === 0 || years === 0) {
        document.getElementById('result').innerText = "₹0.00";
        displayChart(0, 0);
        return;
    }
    
    let interest = (amount * rate * years) / 100;
    let total = amount + interest;
    let formatter = new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' });
    document.getElementById('result').innerText = formatter.format(total);
    
    displayChart(interest, amount);
}

function displayChart(interest, amount) {
    let ctx = document.getElementById("myChart").getContext("2d");
    if (window.myChart) {
        window.myChart.destroy();
    }
    window.myChart = new Chart(ctx, {
        type: "pie",
        data: {
            labels: ["Total Interest", "Principal Amount"],
            datasets: [{
                data: [interest, amount],
                backgroundColor: ["#e63946", "#14213d"],
                borderWidth: 1,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}
