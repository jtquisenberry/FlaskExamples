function getCheckboxes() {
    var array = []
    var checkboxes = document.querySelectorAll('input[type=checkbox]:checked')

    for (var i = 0; i < checkboxes.length; i++) {
      // array.push(checkboxes[i].value)
      c = checkboxes[i]

      array.push(checkboxes[i].id)
    }
    console.log('checkboxes')
    console.log(array)
    return array
}

function saveReviewCalls(row_number) {

    checkbox_ids = getCheckboxes()

    d = JSON.stringify({'checkbox_ids': checkbox_ids})

    $.ajax({
        url: '/' + row_number,
        data: d,
        type: 'POST',
        contentType: 'application/json',
        success: function (data) {
            console.log(data);
            dummy_breakpoint = 0;
        },
        error: function (data) {
            console.log(data);
            dummy_breakpoint = 0;
        }
    }).fail(function ($xhr) {
        var data = $xhr.responseJSON;
        console.log(data);
        dummy_breakpoint = 0;
    });

}