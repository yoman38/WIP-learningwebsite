"""
$(document).ready(function() {
    // Handle form submission for user registration
    $('#registerForm').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: '/user',
            method: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                alert(response.message);
                window.location.href = '/login';
            },
            error: function(response) {
                alert(response.responseJSON.message);
            }
        });
    });

    // Handle form submission for user login
    $('#loginForm').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: '/login',
            method: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                alert(response.message);
                window.location.href = '/home';
            },
            error: function(response) {
                alert(response.responseJSON.message);
            }
        });
    });

    // Handle form submission for course creation
    $('#courseForm').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: '/course',
            method: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                alert(response.message);
                window.location.href = '/home';
            },
            error: function(response) {
                alert(response.responseJSON.message);
            }
        });
    });

    // Handle form submission for content creation
    $('#contentForm').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: '/content',
            method: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                alert(response.message);
                window.location.href = '/course/' + $('#courseId').val();
            },
            error: function(response) {
                alert(response.responseJSON.message);
            }
        });
    });
});
"""
