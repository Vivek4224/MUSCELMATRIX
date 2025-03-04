let selectedAmount = 0;
let customerName = '';
let selectedMethod = '';
let selectedPlanText = ''; 

gsap.from(".container", {
    duration: 1,
    opacity: 0,
    y: -50,
    ease: "power2.out"
});

function updateAmount() {
    const planSelect = document.getElementById('planSelect');
    const amountSpan = document.getElementById('amount');
    selectedAmount = parseInt(planSelect.value) || 0;
    amountSpan.textContent = selectedAmount;
}

function showCreditCard() {
    hideAllForms();
    document.getElementById('credit-card-form').classList.remove('hidden');
    document.querySelectorAll('.payment-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelector('button[onclick="showCreditCard"]').classList.add('active');
    selectedMethod = 'Credit Card';
    animateForm("#credit-card-form");
}

function showDebitCard() {
    hideAllForms();
    document.getElementById('debit-card-form').classList.remove('hidden');
    document.querySelectorAll('.payment-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelector('button[onclick="showDebitCard"]').classList.add('active');
    selectedMethod = 'Debit Card';
    animateForm("#debit-card-form");
}

function showNetBanking() {
    hideAllForms();
    document.getElementById('net-banking-form').classList.remove('hidden');
    document.querySelectorAll('.payment-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelector('button[onclick="showNetBanking"]').classList.add('active');
    selectedMethod = 'Net Banking';
    animateForm("#net-banking-form");
}

function showUPI() {
    hideAllForms();
    document.getElementById('upi-form').classList.remove('hidden');
    document.querySelectorAll('.payment-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelector('button[onclick="showUPI"]').classList.add('active');
    selectedMethod = 'UPI';
    animateForm("#upi-form");
}

function hideAllForms() {
    const forms = document.getElementsByClassName('payment-form');
    for (let form of forms) {
        form.classList.add('hidden');
    }
}

function animateForm(formId) {
    gsap.from(formId, {
        duration: 0.8,
        opacity: 0,
        scale: 0.9,
        ease: "back.out(1.7)"
    });
}

function confirmPayment(method, event) {
    if (event) event.preventDefault(); // Prevent page refresh

    const planSelect = document.getElementById('planSelect');
    const successMessage = document.getElementById('successMessage');
    const successCustomerName = document.getElementById('successCustomerName');
    const successAmount = document.getElementById('successAmount');
    const checkMark = document.querySelector('.check-mark');

    if (planSelect.value === "0") {
        alert("Please select a plan before confirming payment!");
        return;
    }

    let nameInput;
    if (method === 'credit') {
        nameInput = document.getElementById('customerNameCredit').value;
    } else if (method === 'debit') {
        nameInput = document.getElementById('customerNameDebit').value;
    } else if (method === 'netbanking') {
        nameInput = document.getElementById('customerNameNetBanking').value;
    } else if (method === 'upi') {
        nameInput = document.getElementById('customerNameUPI').value;
    }

    if (!nameInput) {
        alert("Please enter your name!");
        return;
    }

    customerName = nameInput; // Update global variable
    selectedAmount = planSelect.value;
    selectedPlanText = planSelect.options[planSelect.selectedIndex].text;
    selectedMethod = method;

    successAmount.textContent = "₹" + selectedAmount;
    successCustomerName.textContent = customerName;

    successMessage.classList.remove('hidden');

    gsap.set(successMessage, { opacity: 0, scale: 0.5 });

    gsap.to(successMessage, {
        opacity: 1,
        scale: 1,
        duration: 1,
        ease: "power3.out"
    });

    if (checkMark) {
        gsap.set(checkMark, { opacity: 0, scale: 0 });
        gsap.to(checkMark, {
            opacity: 1,
            scale: 1,
            rotation: 360,
            duration: 0.8,
            ease: "elastic.out(1, 0.5)",
            delay: 0.5
        });
    }

    setTimeout(() => {
        gsap.to(successMessage, {
            opacity: 0,
            scale: 0.5,
            duration: 1,
            ease: "power1.in",
            onComplete: () => successMessage.classList.add('hidden')
        });
    }, 3000);

    hideAllForms();
    document.querySelectorAll('.payment-btn').forEach(btn => btn.classList.remove('active'));

    downloadReceipt();
}



document.querySelectorAll('.payment-btn').forEach(btn => {
    btn.addEventListener('mouseenter', () => {
        gsap.to(btn, {
            scale: 1.05,
            duration: 0.3,
            ease: "power1.out"
        });
    });
    btn.addEventListener('mouseleave', () => {
        gsap.to(btn, {
            scale: 1,
            duration: 0.3,
            ease: "power1.out"
        });
    });
});

function downloadReceipt() {
    if (window.jspdf) {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF({
            orientation: 'portrait',
            unit: 'mm',
            format: [150, 200]
        });

        doc.setFillColor(13, 6, 38);
        doc.rect(0, 0, 150, 200, "F");

        doc.setFont("helvetica", "bold");
        doc.setFontSize(20);
        doc.setTextColor(53, 47, 230);
        doc.text("MuscleMatrix Gym", 75, 20, { align: "center" });

        doc.setFont("helvetica", "normal");
        doc.setFontSize(14);
        doc.text("Membership Payment Receipt", 75, 30, { align: "center" });

        doc.setDrawColor(255, 255, 255);
        doc.line(20, 35, 130, 35);

        doc.setFontSize(12);
        let yPosition = 50;
        doc.text("Customer Name: " + customerName, 20, yPosition);
        yPosition += 10;
        doc.text("Selected Plan: " + selectedPlanText, 20, yPosition);
        yPosition += 10;
        doc.text("Amount Paid: ₹" + selectedAmount, 20, yPosition);
        yPosition += 10;
        doc.text("Payment Method: " + selectedMethod, 20, yPosition);
        yPosition += 10;
        doc.text("Date & Time: " + new Date().toLocaleString(), 20, yPosition);
        yPosition += 10;

        doc.line(20, yPosition, 130, yPosition);
        yPosition += 10;

        doc.setFontSize(14);
        doc.setTextColor(255, 215, 0);
        doc.text("Thank you for choosing MuscleMatrix Gym!", 75, yPosition, { align: "center" });

        doc.save(`Payment_Receipt_${customerName}.pdf`);
    } else {
        console.error("jsPDF library is not loaded.");
        alert("PDF library is missing. Please ensure the jsPDF script is included in your HTML.");
    }
}

function getSelectedMethod() {
    return selectedMethod || "Unknown Method";
}