$(document).ready(function() {
    const employmentTypeField = $('#id_employment_type');
    const companyField = $('#id_company_name').closest('.form-group');
    const clearanceLevelField = $('#id_ip_clearance_level').closest('.form-group');

    // Initially hide fields
    companyField.hide();
    clearanceLevelField.hide();

    // Toggle visibility and required attribute based on Employment Type selection
    function toggleRequiredFields() {
        if (employmentTypeField.val() === 'other') {
            companyField.show();
            clearanceLevelField.show();
            $('#id_company_name').prop('required', true);
            $('#id_ip_clearance_level').prop('required', true);
        } else {
            companyField.hide();
            clearanceLevelField.hide();
            $('#id_company_name').prop('required', false);
            $('#id_ip_clearance_level').prop('required', false);
        }
    }

    // Trigger function on page load and when Employment Type changes
    employmentTypeField.change(toggleRequiredFields);
    toggleRequiredFields();  // Initial call on page load
});
