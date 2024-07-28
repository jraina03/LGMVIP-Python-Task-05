$(document).ready(function() {
    // Function to add message to the chat window
    function addMessage(message, isUser) {
      var messageClass = isUser ? 'user-message' : 'response-message';
      var messageContainer = $('#messageContainer');
      messageContainer.append('<div class="' + messageClass + '">' + message + '</div>');
      // Scroll to the bottom of the container
      messageContainer.scrollTop(messageContainer.prop("scrollHeight"));
    }
  
    // Function to handle form submission
    $('#messageForm').submit(function(event) {
      event.preventDefault(); // Prevent default form submission
  
      var message = $('#messageInput').val().trim();
      if (message !== '') {
        // Add user message to the chat container
        addMessage(message, true);
  
        // Make AJAX request to the API endpoint
        $.ajax({
          url: '/api',
          type: 'POST',
          contentType: 'application/x-www-form-urlencoded',
          data: { message: message }, // Send form data
          success: function(response) {
            // Add response message to the chat container
            addMessage(response.response, false);
          },
          error: function(xhr, status, error) {
            console.error('Error:', error);
          }
        });
  
        // Clear the input field
        $('#messageInput').val('');
      }
    });
  });
  