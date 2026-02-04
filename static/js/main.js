// main.js - Essential helper logic for Smart Civic Issue Reporter

// Auto-capture GPS location when report page loads
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on the report page
    if (document.getElementById('latitude') && document.getElementById('longitude')) {
        captureGPSLocation();
    }
    
    // Setup image preview functionality
    const imageInput = document.getElementById('image');
    if (imageInput) {
        imageInput.addEventListener('change', previewImage);
    }
});

/**
 * Capture user's GPS location using browser's Geolocation API
 */
function captureGPSLocation() {
    const gpsStatus = document.getElementById('gps-status');
    const submitBtn = document.getElementById('submitBtn');
    
    if (!navigator.geolocation) {
        gpsStatus.className = 'alert alert-danger';
        gpsStatus.innerHTML = '❌ GPS not supported by your browser';
        return;
    }
    
    gpsStatus.className = 'alert alert-info';
    gpsStatus.innerHTML = '📍 Capturing your location...';
    
    navigator.geolocation.getCurrentPosition(
        // Success callback
        function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            
            // Store in hidden fields for form submission
            document.getElementById('latitude').value = latitude;
            document.getElementById('longitude').value = longitude;
            
            // Display in read-only fields
            document.getElementById('lat_display').value = latitude.toFixed(6);
            document.getElementById('long_display').value = longitude.toFixed(6);
            
            // Update status message
            gpsStatus.className = 'alert alert-success';
            gpsStatus.innerHTML = '✅ Location captured successfully!';
            
            // Enable submit button
            submitBtn.disabled = false;
        },
        // Error callback
        function(error) {
            let errorMessage = '';
            
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    errorMessage = '❌ Location permission denied. Please enable location access.';
                    break;
                case error.POSITION_UNAVAILABLE:
                    errorMessage = '❌ Location information unavailable.';
                    break;
                case error.TIMEOUT:
                    errorMessage = '❌ Location request timed out.';
                    break;
                default:
                    errorMessage = '❌ Unknown error occurred while getting location.';
                    break;
            }
            
            gpsStatus.className = 'alert alert-danger';
            gpsStatus.innerHTML = errorMessage + ' <br><small>You can manually enter coordinates if needed.</small>';
            
            // Allow manual submission without GPS (backend should validate)
            // submitBtn.disabled = false; // Uncomment if you want to allow manual entry
        },
        // Options
        {
            enableHighAccuracy: true,
            timeout: 10000,
            maximumAge: 0
        }
    );
}

/**
 * Preview uploaded image before form submission
 */
function previewImage(event) {
    const file = event.target.files[0];
    const previewContainer = document.getElementById('imagePreviewContainer');
    const previewImg = document.getElementById('imagePreview');
    
    if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            previewImg.src = e.target.result;
            previewContainer.style.display = 'block';
        };
        
        reader.readAsDataURL(file);
    } else {
        previewContainer.style.display = 'none';
    }
}

/**
 * Optional: Form validation before submission
 */
function validateForm(event) {
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;
    
    if (!latitude || !longitude) {
        event.preventDefault();
        alert('Please wait for GPS location to be captured before submitting.');
        return false;
    }
    
    return true;
}

// Attach validation to form if it exists
const reportForm = document.getElementById('reportForm');
if (reportForm) {
    reportForm.addEventListener('submit', validateForm);
}
