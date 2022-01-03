//on click function for the ingredient selector buttons
//upon clicking the button the color changes to green and an object is created with the 'food' field
//being populated by the button value. When the same button is clicked again the previously created object is deleted
// if request method is post AND action is whatever, then clear > separate from current if statement
$(document).off().on('click', '.empty', function (e) {
    $(this).toggleClass('select-button-gray select-button-green')
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/test/select/',
        data: {
            value: $(this).val(),
            testvalue: 'check',
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),

        },
        success: function () {
            console.log("success"); // another sanity check
        },
    })
})


function testFunction() {
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/test/select/',
        data: {
            reload: 'true',
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function () {
            console.log('reload info trasmitted')
        }
    })
}