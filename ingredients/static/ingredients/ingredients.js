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


// ------------------------------------------------------------------------------------------------------------------------
$(document).ready(function(){
  $( ".form-inline" ).each(function(){
      $(this).find(".empty:gt(8)" ).addClass('hide');
      $(this).find(".empty").eq(9).after('<button class="select-button-green hidecontent">Show more</button>');//add a unique id to link

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

