document.addEventListener('DOMContentLoaded', function() {
    // Sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Initialize select elements
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    // Initialize datepicker only if present on the page
    var dateElems = document.querySelectorAll('.datepicker');
    if (dateElems.length > 0) {
        console.log('Initializing datepicker...');

        dateElems.forEach(function(elem) {
            let defaultDate = null;

            // If the field has a value, convert it to a date object
            if (elem.value) {
                let parts = elem.value.split('-');
                if (parts.length === 3) {
                    defaultDate = new Date(parts[2], parts[1] - 1, parts[0]);  // Create a date from dd-mm-yyyy
                }
            }

            M.Datepicker.init(elem, {
                format: 'dd-mm-yyyy',  // Adjusted format to match the desired format (dd-mm-yyyy)
                autoClose: true,
                defaultDate: defaultDate,  // Use the pre-populated value if present
                setDefaultDate: !!defaultDate,  // Only set default if the date exists
                onClose: function() {
                    console.log("Selected date:", elem.value);
                }
            });
        });
    }

    // Initialize timepicker only if present on the page
    var timeElems = document.querySelectorAll('.timepicker');
    if (timeElems.length > 0) {
        console.log('Initializing timepicker...');

        timeElems.forEach(function(elem) {
            M.Timepicker.init(elem, {
                twelveHour: false,
                defaultTime: elem.value || 'now',  // Use pre-populated time if available
                showClearBtn: true,
                onCloseEnd: function() {
                    console.log("Selected time:", elem.value);
                }
            });
        });
    }

    // Log the admin dashboard link to ensure it is rendered
    let adminLink = document.querySelector('a[href="/admin_dashboard"]');
    if (adminLink) {
        console.log("Admin Dashboard link is rendered:", adminLink);
    } else {
        console.log("Admin Dashboard link not found");
    }
});
