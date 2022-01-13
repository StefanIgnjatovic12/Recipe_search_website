//on click function for the ingredient selector buttons
//upon clicking the button the color changes to green and an object is created with the 'food' field
//being populated by the button value. When the same button is clicked again the previously created object is deleted
// if request method is post AND action is whatever, then clear > separate from current if statement
$(document).off().on('click', '.empty', function (e) {
    $(this).toggleClass('select-button-gray select-button-green')
    e.preventDefault();
    var button_color
    if ($(this).hasClass('select-button-gray')) {
        button_color = 'gray'
    } else if ($(this).hasClass('select-button-green')) {
        button_color = 'green'
    }
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/test/select/',
        data: {
            value: $(this).val(),
            button_state: 'clicked',
            button_color: button_color,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),

        },
        success: function () {
            console.log("success");

        },
    })
})



function detectReload() {
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


// ------------------------------------------------------------------------------------------------------------------------
$(document).ready(function(){
  $( ".form-inline" ).each(function(){
      $(this).find(".empty:gt(8)" ).addClass('hide');
      $(this).find(".empty").eq(9).after('<button class="show-more-button hidecontent">Show more</button>');//add a unique id to link

  });
});


$(document).on('click','.hidecontent',function(e){
  e.preventDefault();
  //removes the hide class from the 9 buttons
  $(this).closest('.form-inline').find('.hide, .test').toggleClass('hide test');
  $(this).closest('.media-body').find('.arrow').toggleClass('triangle_down triangle_up')
     //adds the hide class to the show more button
	 $(this).addClass('hide');
});
// ------------------------------------------------------------------------------------------------------------------------


// changing arrow from up to down
$(document).on('click', '.arrow', function (e) {
    $(this).closest('.media-body').find('.hide, .test').not('.hidecontent').toggleClass('hide test');
    $(this).toggleClass('triangle_down triangle_up')
    $(this).closest('.media-body').find('.hidecontent').toggleClass('hide')

    // e.preventDefault();

})

//Sliding column
$(function(){
    $('.test-button').click(function(){
        $('.sliding-navbar').toggleClass('sliding-navbar--open hide');
    });


});
//on clicking the favorite button, the forloop counter value will be transmitted
//the value corresponds to the index of the recipe within the dictionary passed into sessions
$(document).on('click', '.favorite', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/test/select/',
        data: {
            recipe_id: $(this).val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),

        },
        success: function () {
            console.log("recipe ID sent");

        },
    })
})

//toggle class when favorite button is clicked
$(document).on('click', '.card-action', function (e) {
    $(this).toggleClass('card-color1 card-color2')
    e.preventDefault();
})