document.addEventListener("DOMContentLoaded", function () {
    // Set the minimum date to today
    const dateInput = document.getElementById("date");
    const today = new Date().toISOString().split('T')[0];
    document.getElementById("date").setAttribute("min", today);
    dateInput.value = today;

    const selectTime = document.getElementById("time");

    // Define available times in 45-minute intervals (24-hour format)
    const timeSlots = [
        "08:00", "08:45", "09:30", "10:15", "11:00", "11:45",
        "12:30", "13:15", "14:00", "14:45", "15:30", "16:15",
        "17:00", "17:45", "18:30", "19:15", "20:00"
    ];

    // Convert 24-hour time to 12-hour AM/PM format
    function formatTime(time) {
        let [hour, minute] = time.split(":").map(Number);
        let period = hour >= 12 ? "PM" : "AM";
        hour = hour % 12 || 12; // Convert to 12-hour format
        return `${hour}:${minute.toString().padStart(2, "0")} ${period}`;
    }

    const now = new Date();
    const currentHour = now.getHours();
    const currentMinutes = now.getMinutes();

    selectTime.innerHTML = "";

    // Generate time options dynamically
    timeSlots.forEach(time => {
        const [hour, minutes] = time.split(":").map(Number);
        
        if (hour > currentHour || (hour === currentHour && minutes > currentMinutes) || today !== now.toISOString().split('T')[0]) {
            const option = document.createElement("option");
            option.value = time;
            option.textContent = formatTime(time);
            selectTime.appendChild(option);
        }
    });

    // Set the default selected time to the nearest available slot
    if (selectTime.options.length > 0) {
        selectTime.selectedIndex = 0;
    }
});
