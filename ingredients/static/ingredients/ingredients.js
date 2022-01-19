function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//on click function for the ingredient selector buttons
//upon clicking the button the color changes to green and an object is created with the 'food' field
//being populated by the button value. When the same button is clicked again the previously created object is deleted
// if request method is post AND action is whatever, then clear > separate from current if statement
$(document).off().on('click', '.empty', function (e) {
    $(this).toggleClass('select-button-gray select-button-green')

    e.preventDefault();
    let button_color
    if ($(this).hasClass('select-button-gray')) {
        button_color = 'gray'
    } else if ($(this).hasClass('select-button-green')) {
        button_color = 'green';

    }
    $.ajax({
        type: 'POST',
        url: 'select/',
        data: {
            value: $(this).val(),
            button_state: 'clicked',
            button_color: button_color,
            csrfmiddlewaretoken: getCookie('csrftoken')

        },
        success: function () {
            console.log("success");

        },
    })
})

$(document).on('click', '#mybtn', function () {
    function ajaxCall() {
        $.ajax({
            headers: {csrfmiddlewaretoken: getCookie('csrftoken')},
            type: 'GET',
            dataType: 'json',
            url: 'choicesstatus/',
            data: {data},

            success: function () {
                console.log('data received')



            },
        })

        function check(data) {
            if (data.choices == 'full') {
                    $('.submit-form').removeAttr('onsubmit')
                } else if ($('.submit-form').not('[onsubmit]')) {
                    $.fn.ajaxCall()
                    $('.submit-form').attr('onsubmit', 'return false;')
                }
        }
    }
})


//function which detects if the page has been reloaded and notifies the backend
function detectReload() {
    $.ajax({
        type: 'POST',
        url: 'select/',
        data: {
            reload: 'true',
            csrfmiddlewaretoken: getCookie('csrftoken')
        },
        success: function () {
            console.log('reload info trasmitted')
        }
    })
}

//Function which is responsible for hiding and revealing the ingredient buttons;
//adds the hide class after the 8th button and then inserts the show more button
// ------------------------------------------------------------------------------------------------------------------------
$(document).ready(function () {
    $(".form-inline").each(function () {
        $(this).find(".empty:gt(8)").addClass('hide');
        $(this).find(".empty").eq(9).after('<button class="show-more-button hidecontent">Show more</button>');//add a unique id to link

    });
});


$(document).on('click', '.hidecontent', function (e) {
    e.preventDefault();
    //removes the hide class from the 9 buttons
    $(this).closest('.form-inline').find('.hide, .unhide').toggleClass('hide unhide');
    $(this).closest('.media-body').find('.arrow').toggleClass('triangle_down triangle_up')
    //adds the hide class to the show more button
    $(this).addClass('hide');
});
// ------------------------------------------------------------------------------------------------------------------------


// changing arrow from up to down
$(document).on('click', '.arrow', function () {
    $(this).closest('.media-body').find('.hide, .unhide').not('.hidecontent').toggleClass('hide test');
    $(this).toggleClass('triangle_down triangle_up')
    $(this).closest('.media-body').find('.hidecontent').toggleClass('hide')


});


//on clicking the favorite button, the forloop counter value will be transmitted
//the value corresponds to the index of the recipe within the dictionary passed into sessions
//checks if the card has class unfavorite which means that its a card on the favorite page > in that case remove it from the page on click
$(document).on('click', '.favorite', function (e) {
    $(this).toggleClass('card-color1 card-color2')
    if ($(this).closest('.col').hasClass('unfavorite')) {
        $(this).closest('.col').remove();
    }
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/select/',
        data: {
            recipe_id: $(this).attr('id'),
            csrfmiddlewaretoken: getCookie('csrftoken')

        },
        success: function () {
            console.log("recipe ID sent");


        },
    })
});


//get search value and use it to click button
$(document).on('click', '.search-button', function (e) {
    let search_value = $('#search-bar').val()
    $('#search-bar').val('')
    $("[value='" + search_value + "']").removeClass('select-button-gray').addClass('select-button-green')
    // $("[value='" + search_value + "']").addClass('select-button-green')
    e.preventDefault();
    let button_color
    if ($("[value='" + search_value + "']").hasClass('select-button-gray')) {
        button_color = 'gray'
    } else if ($("[value='" + search_value + "']").hasClass('select-button-green')) {
        button_color = 'green'
    }
    $.ajax({
        type: 'POST',
        url: 'select/',
        data: {
            value: search_value,
            button_state: 'clicked',
            button_color: button_color,
            csrfmiddlewaretoken: getCookie('csrftoken')

        },
        success: function () {
            console.log("testing search feature");


        },
    })
});

//function which changes show full recipe button text and adjusts the way the header text is presented depending on if the card is expanded or not
function toggleText(elem) {
    $(elem).closest('.card').toggleClass('expand')
    $(elem).closest('.card').find('.ingredients-header-card-text, .ingredients-header-card-text2 ').toggleClass('ingredients-header-card-text ingredients-header-card-text2')

    //  swaps the text
    if (elem.innerText === 'See more') {
        elem.innerText = 'See less'
    }
    //swaps the text and collapses the ingredient list upon clicking hide full recipe if it's expanded
    else if (elem.innerText === 'See less') {
        elem.innerText = 'See more'

        if ($(elem).closest('.card').find('.ingredient-list-group').hasClass('show')) {
            $(elem).closest('.card').find('.triangle-card').trigger('click')
        }

    }


}

// same function as above but for cards on favorite page
function toggleTextFavorite(elem) {
    $(elem).closest('.card').toggleClass('favorite-button')
    $(elem).closest('.card').find('.ingredients-header-card-text, .ingredients-header-card-text2 ').toggleClass('ingredients-header-card-text ingredients-header-card-text2')

    //  swaps the text
    if (elem.innerText === 'See more') {
        elem.innerText = 'See less'
    }
    //swaps the text and collapses the ingredient list upon clicking hide full recipe if it's expanded
    else if (elem.innerText === 'See less') {
        elem.innerText = 'See more'

        if ($(elem).closest('.card').find('.ingredient-list-group').hasClass('show')) {
            $(elem).closest('.card').find('.triangle-card').trigger('click')
        }

    }


}
