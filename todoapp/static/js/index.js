document.addEventListener('DOMContentLoaded', function(){
    console.log(localStorage.getItem('mail'));
    console.log('Hi there');

    var buttons = document.querySelectorAll(".ac, .turn_On, .turn_Off, .account_button");

    buttons.forEach(function(button) {
        button.addEventListener("click", function () {
            if (button.id === 'turn_Off' || button.id === 'turn_On' || button.id === "delete") {
                console.log('/' + button.id + '/' + button.name + '/');
                fetch('/' + button.id + '/' + button.name + '/')
                setTimeout(function(){
                    window.location.href = "/index/";
                }, 100);
            } else if (button.name === "account_button") {
                console.log("Goodbye");
                localStorage.removeItem('mail');
                localStorage.removeItem('password');
                console.log("removed");
                window.location.href = '/';
            } else {
                console.error("Error");
            }
        });
    });
});