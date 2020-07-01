// function submitForm() {

// }

// $(function(){
//     $("#payment-form").submit(submitForm)
// })

function showErrors(message) {
    const messageArea = $("#message-error");
    messageArea.text(message);
    messageArea.show();
};
function hideErrors() {
    const messageArea = $("#message-error");
    messageArea.hide();
};

$(function() {
    $("#payment-form").submit(function() {
        const btnSubmit = $("#submit_payment_btn");

        // Prevent double-click
        btnSubmit.attr("disabled", true);

        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };

    Stripe.createToken(card, function(status, response) {
        btnSubmit.attr("disabled", false);

        if (status === 200) {
            hideErrors();
            $("#id_stripe_id").val(response.id);

            // Prevent the credit card details from being submitted
            // to our server
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');

            form.submit();
        } else {
            showErrors(response.error.message);
        }
    });
    return false;
    });
});