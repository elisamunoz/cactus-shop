const showErrors = (message) => {
    const messageArea = $("#message-error");
    messageArea.text(message);
    messageArea.show();
};
const hideErrors = () => {
    const messageArea = $("#message-error");
    messageArea.hide();
};

$(() => {
    $("#payment-form").submit(() => {
        const btnSubmit = $("#submit_payment_btn");

        // Prevent double-click
        btnSubmit.attr("disabled", true);

        const form = this;
        const card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };

    Stripe.createToken(card, (status, response) => {
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