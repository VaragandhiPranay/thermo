// jQuery ready function to ensure the document is fully loaded before running scripts
$(document).ready(function() {
    // Employment type selection to toggle visibility of company and IP clearance fields
    const employmentTypeField = $('#id_employment_type');
    const companyField = $('#id_company_name').closest('.form-group');
    const clearanceLevelField = $('#id_ip_clearance_level').closest('.form-group');

    // Show or hide company name and IP clearance fields based on employment type
    function toggleCompanyAndClearance() {
        if (employmentTypeField.val() === 'other') {
            companyField.show();
            clearanceLevelField.show();
        } else {
            companyField.hide();
            clearanceLevelField.hide();
        }
    }

    employmentTypeField.change(toggleCompanyAndClearance);
    toggleCompanyAndClearance(); // Initial call on page load

    // Search functionality for filtering user data table rows
    $('#searchInput').on('keyup', function() {
        const value = $(this).val().toLowerCase();
        $('#userDataTable tr').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});
