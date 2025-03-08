document.addEventListener("DOMContentLoaded", function () {
    const bookingForm = document.getElementById("service-booking-form");
    const checkboxes = document.querySelectorAll(".service-checkbox");
    const totalPriceElement = document.getElementById("total-price");

    function generateReferenceID() {
        return "REF-" + Math.floor(100000 + Math.random() * 900000);
    }

    function updateTotal() {
        let total = 0;

        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                total += parseFloat(checkbox.getAttribute("data-price"));
            }
        });

        totalPriceElement.textContent = `$${total}`;
    }

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", updateTotal);
    });

    bookingForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission
        
        // Collect user details
        const name = document.getElementById("name").value;
        const phone = document.getElementById("phone").value;
        const carDetails = `${document.querySelector("input[placeholder='mark']").value} - ` +
                           `${document.querySelector("input[placeholder='model']").value} - ` +
                           `${document.querySelector("input[placeholder='year']").value}`;

        // Get selected services
        let services = [];
        let total = 0;

        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                let serviceName = checkbox.value;
                let servicePrice = parseFloat(checkbox.getAttribute("data-price"));
                services.push({ name: serviceName, price: servicePrice });
                total += servicePrice;
            }
        });

        // Generate reference ID
        const refID = generateReferenceID();

        // Display Invoice
        document.getElementById("ref-id").textContent = refID;
        document.getElementById("invoice-name").textContent = name;
        document.getElementById("invoice-phone").textContent = phone;
        document.getElementById("invoice-car").textContent = carDetails;
        document.getElementById("invoice-total").textContent = `$${total}`;

        let serviceList = document.getElementById("invoice-services");
        serviceList.innerHTML = ""; // Clear previous list

        services.forEach(service => {
            let li = document.createElement("li");
            li.textContent = `${service.name} - $${service.price}`;
            serviceList.appendChild(li);
        });

        // Show invoice
        document.getElementById("invoice").style.display = "block";
    });
});


/* <!-- Invoice Container (Hidden Initially) -->
<div id="invoice" style="display: none;">
    <h2>Booking Invoice</h2>
    <p><strong>Reference ID:</strong> <span id="ref-id"></span></p>
    <p><strong>Name:</strong> <span id="invoice-name"></span></p>
    <p><strong>Phone:</strong> <span id="invoice-phone"></span></p>
    <p><strong>Car Details:</strong> <span id="invoice-car"></span></p>
    <h3>Services Selected:</h3>
    <ul id="invoice-services"></ul>
    <h3>Total Price: <span id="invoice-total"></span></h3>
    <button onclick="window.print()">Print Invoice</button>
</div>
 */