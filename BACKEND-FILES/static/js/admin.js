// JavaScript source code
function logout() {
    window.location.href = "login.html";
}


function stats() {
    var ctx = document.getElementById("div_content");
    var div_content = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            datasets: [{
                data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#007bff',
                borderWidth: 4,
                pointBackgroundColor: '#007bff'
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: false
                    }
                }]
            },
            legend: {
                display: false,
            }
        }
    });
}

function dash() {
    var ctx = document.getElementById("myChart");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}


function accounts() {
    var newactive = $(this).text();
    if (newactive.text == "Accounts") {
        $("#content").load("login.html");
        $("#content").load(url("../login.html"));
    }
}


$(document).ready(function () {
    $(".nav a").on("click", function () {

        var newactive = $.trim($(this).text());
        console.log(newactive);

        $(".nav a").removeClass("active");
        $(this).addClass("active");

        $(".h2").text(newactive);

        if (newactive == "Dashboard") {
            $("#div_content").text("Welcome");
        }

        else if (newactive == "Edit Accounts") {
            $("#div_content").load("editaccount.html");
        }

        else if (newactive == "Schedule") {
            $("#div_content").load("test.html");
        }

        else if (newactive == "Account Info") {
            $("#div_content").text("Account info page");
        }

        else if (newactive == "Create Account") {
            $("#div_content").load("createaccount.html");
        }

        else if (newactive == "Statistics") {
            $("#div_content").load("statistics.html");
        }


    })
});